from django.urls import path
from user_app.views import RegistrationUserView

urlpatterns = [
    path('create/', RegistrationUserView.as_view()),
]