from django.urls import reverse
from rest_framework.test import APIClient
from blog.settings import USER_LOGIN_URL
from posts.models import User, Post


class TestSetUpData():

    def setUpData(self):

        self.client = APIClient()
        post_user = User(username='post_user', password='secret', email='post_user@gmail.com')
        post_user.save()
        reg_url = reverse('registration')
        self.client.post(reg_url, {
            'username': 'sany',
            'password': 'sany',
            'password_confirm': 'sany',
            'email': 'sany@gmail.com'}, format='json')

        Post.objects.create(title='First post', text='Text for first post', user=post_user)
        Post.objects.create(title='Second post', text='Text for second post', user=post_user)
        Post.objects.create(title='Third post', text='Text for third post', user=post_user)

        user = self.client.post(f'/{USER_LOGIN_URL}', {'username': 'sany', 'password': 'sany'}, format='json')
        token = user.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
