from blog.settings import USER_LOGIN_URL
from blog.settings import TIME_ZONE
from user_app.models import UserActions
from django.contrib.auth import get_user_model
from datetime import datetime
import pytz
User = get_user_model()
tz = pytz.timezone(TIME_ZONE)


def user_actions_middleware(get_response):

    def middleware(request):
        response = get_response(request)
        print(request.path)

        if request.user.is_authenticated and request.path != f'/{USER_LOGIN_URL}':
            try:
                actions = UserActions.objects.get(user_id=request.user.id)
                actions.last_action = datetime.now(tz)
                actions.save()
            except:
                UserActions(user=request.user, login_time=datetime.now(tz), last_action=datetime.now()).save(tz)

        return response

    return middleware