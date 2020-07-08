from django.urls import path
from user_app.views import RegistrationUserView, UserActionsView

urlpatterns = [
    path('user/register/', RegistrationUserView.as_view()),
    path('user/actions/<int:pk>/', UserActionsView.as_view()),
]