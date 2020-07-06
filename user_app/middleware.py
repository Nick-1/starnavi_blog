from blog.settings import USER_LOGIN_URL
from user_app.models import UserActions
from django.contrib.auth import get_user_model
User = get_user_model()


def simple_middleware(get_response):

    def middleware(request):
        response = get_response(request)
        if request.path != f'/{USER_LOGIN_URL}':
            actions = UserActions.objects.get(user_id=request.user.id)
            actions.last_action = request.path
            actions.save()
        return response

    return middleware