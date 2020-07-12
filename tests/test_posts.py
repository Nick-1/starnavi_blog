from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from constants import POSTS_URL, LIKE_URL
from tests.setupdata import TestSetUpData
User = get_user_model()


class PostsTest(TestCase, TestSetUpData):

    def setUp(self):
        TestSetUpData.setUpData(self)

    def test_post_get_all(self):
        response = self.client.get(f'/{POSTS_URL}', data={'format': 'json'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_get_one_(self):
        response = self.client.get(f'/{POSTS_URL}1/', data={'format': 'json'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create(self):
        response = self.client.post(f'/{POSTS_URL}', {'title': 'title', 'text': 'text'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_change(self):
        post = self.client.post(f'/{POSTS_URL}', {'title': 'new title', 'text': 'new text'})
        response = self.client.patch(f'/{POSTS_URL}{post.data["id"]}/', {'new title': 'new title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_delete(self):
        post = self.client.post(f'/{POSTS_URL}', {'title': 'title', 'text': 'text'})
        delete = self.client.delete(f'/{POSTS_URL}{post.data["id"]}/')
        self.assertEqual(delete.status_code, status.HTTP_204_NO_CONTENT)

    def test_post_permissions_change(self):
        user_2_post = self.client.post(f'/{POSTS_URL}', {'title': 'title', 'text': 'text'})
        TestSetUpData.user_registration(self, 'user_3')
        TestSetUpData.user_login(self, 'user_3')
        try_to_change = self.client.patch(f'/{POSTS_URL}{user_2_post.data["id"]}/', {'new title': 'new title'})
        self.assertEqual(try_to_change.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_permissions_delete(self):
        user_2_post = self.client.post(f'/{POSTS_URL}', {'title': 'title', 'text': 'text'})
        TestSetUpData.user_registration(self, 'user_3')
        TestSetUpData.user_login(self, 'user_3')
        try_to_delete = self.client.delete(f'/{POSTS_URL}{user_2_post.data["id"]}/')
        self.assertEqual(try_to_delete.status_code, status.HTTP_403_FORBIDDEN)

    def test_like_like_unlike(self):
        like = self.client.post(f'/{LIKE_URL}', {'post': '1'})
        self.assertEqual(like.status_code, status.HTTP_201_CREATED)
        unlike = self.client.delete(f'/{LIKE_URL}1/', data={'format': 'json'})
        self.assertEqual(unlike.status_code, status.HTTP_204_NO_CONTENT)

    def test_like_permissions(self):
        self.client.post(f'/{LIKE_URL}', {'post': '2'})
        TestSetUpData.user_registration(self, 'user_3')
        TestSetUpData.user_login(self, 'user_3')
        user_1_unlike = self.client.delete(f'/{LIKE_URL}2/', data={'format': 'json'})
        self.assertEqual(user_1_unlike.status_code, status.HTTP_400_BAD_REQUEST)

    def test_like_unique(self):
        first_like = self.client.post(f'/{LIKE_URL}', {'post': '3'})
        self.assertEqual(first_like.status_code, status.HTTP_201_CREATED)
        second_like = self.client.post(f'/{LIKE_URL}', {'post': '3'})
        self.assertEqual(second_like.status_code, status.HTTP_400_BAD_REQUEST)
