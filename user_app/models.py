from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class UserActions(models.Model):
    user = models.OneToOneField(User, related_name='log_actions', on_delete=models.CASCADE)
    login_time = models.DateTimeField()
    last_action = models.CharField(max_length=300)
