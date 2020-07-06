from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.views import TokenViewBase

from user_app.serializers import RegistrationSerializer, CustomTokenObtainPairSerializer


class RegistrationUserView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer


class LoginView(TokenViewBase):
    serializer_class = CustomTokenObtainPairSerializer
