from django.urls import reverse
from rest_framework.test import APIClient
from blog.settings import USER_LOGIN_URL
from posts.models import User, Post


class TestSetUpData():

    def user_registration(self, username):
        reg_url = reverse('registration')
        self.client.post(reg_url, {
            'username': username,
            'password': username,
            'password_confirm': username,
            'email': f'{username}@gmail.com'}, format='json')

    def user_login(self, username):
        user = self.client.post(f'/{USER_LOGIN_URL}', {'username': username, 'password': username}, format='json')
        token = user.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def setUpData(self):
        self.client = APIClient()
        post_user = User(username='post_user', password='secret', email='post_user@gmail.com')
        post_user.save()

        Post.objects.create(title='First post', text='Text for first post', user=post_user)
        Post.objects.create(title='Second post', text='Text for second post', user=post_user)
        Post.objects.create(title='Third post', text='Text for third post', user=post_user)

        self.user_registration('user_2')
        self.user_login('user_2')
