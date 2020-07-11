from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from posts.models import Post
from constants import POSTS_URL, LIKE_URL, USER_LOGIN_URL
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

        user = self.client.post(f'/{USER_LOGIN_URL}', {'username': 'sany', 'password': 'sany'}, format='json')
        token = user.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_get_all_posts(self):
        response = self.client.get(f'/{POSTS_URL}', data={'format': 'json'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_post(self):
        response = self.client.get(f'/{POSTS_URL}1/', data={'format': 'json'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_like_unlike_post(self):
        like = self.client.post(f'/{LIKE_URL}', {'post': '1'})
        self.assertEqual(like.status_code, status.HTTP_201_CREATED)
        unlike = self.client.delete(f'/{LIKE_URL}1/', data={'format': 'json'})
        self.assertEqual(unlike.status_code, status.HTTP_204_NO_CONTENT)
