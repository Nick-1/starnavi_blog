import datetime

from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()


class PostsTest(TestCase):

    def setUp(self):
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

        login_url = reverse('jwt-login')
        user = self.client.post(login_url, {'username': 'sany', 'password': 'sany'}, format='json')
        token = user.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_get_all_likes_count(self):
        date = datetime.date.today()
        self.client.post('/api/v1/like/', {'post': '1'})
        self.client.post('/api/v1/like/', {'post': '2'})
        self.client.post('/api/v1/like/', {'post': '3'})
        response = self.client.get(f'/api/v1/likescount/?date_from={date}&date_to={date}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        day = response.data['results'][0]['day']
        count = response.data['results'][0]['count']
        self.assertEqual(day, str(date))
        self.assertEqual(count, 3)
