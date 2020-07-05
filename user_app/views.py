from django.shortcuts import render
from rest_framework import generics

from user_app.serializers import RegistrationSerializer


class RegistrationUserView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer



