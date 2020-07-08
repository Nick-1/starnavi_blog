from datetime import datetime
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user_app.models import UserActions
from blog.settings import TIME_ZONE
import pytz
tz = pytz.timezone(TIME_ZONE)

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password_replay = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_replay']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password_replay = self.validated_data['password_replay']

        if password != password_replay:
            raise serializers.ValidationError({'password': 'Password must match.'})
        user.set_password(password)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        try:
            actions = UserActions.objects.get(user_id=self.user.id)
            actions.login_time = datetime.now(tz)
            actions.last_action = datetime.now(tz)
            actions.save()
        except:
            UserActions(user=self.user, login_time=datetime.now(tz), last_action=datetime.now()).save(tz)
        return data


class UserActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActions
        fields = ['login_time', 'last_action']
