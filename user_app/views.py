from rest_framework import generics
from rest_framework_simplejwt.views import TokenViewBase
from user_app.models import UserActions
from user_app.permissions import CurrentUserOrAdmin
from user_app.serializers import RegistrationSerializer, CustomTokenObtainPairSerializer, UserActionsSerializer


class RegistrationUserView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer


class LoginView(TokenViewBase):
    serializer_class = CustomTokenObtainPairSerializer


class UserActionsView(generics.RetrieveAPIView):
    serializer_class = UserActionsSerializer
    queryset = UserActions.objects.all()
    permission_classes = (CurrentUserOrAdmin, )
