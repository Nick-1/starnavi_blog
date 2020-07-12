from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from constants import POSTS_URL, LIKE_URL
from tests.setupdata import TestSetUpData

User = get_user_model()


class PostsTest(TestCase, TestSetUpData):

    def setUp(self):
        TestSetUpData.setUpData(self)

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
