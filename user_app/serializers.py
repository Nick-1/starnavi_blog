from datetime import datetime

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from blog.settings import USER_LOGIN_URL
from user_app.models import UserActions

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match.'})
        user.set_password(password)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        actions = UserActions.objects.get(user_id=self.user.id)
        if actions:
            actions.login_time = datetime.now()
            actions.last_action = USER_LOGIN_URL
            actions.save()
        else:
            UserActions(user=self.user, login_time=datetime.now(), last_action=USER_LOGIN_URL).save()
        return data