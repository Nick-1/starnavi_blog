from django.urls import path
from user_app.views import RegistrationUserView

urlpatterns = [
    path('user/register/', RegistrationUserView.as_view()),
]