from django.test import TestCase
from rest_framework import status
from tests.setupdata import TestSetUpData
from constants import get_user_actions_url


class PostsTest(TestCase, TestSetUpData):

    def setUp(self):
        TestSetUpData.setUpData(self)

    def test_actions_get(self):
        response = self.client.get(get_user_actions_url(1))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actions_permissions(self):
        TestSetUpData.user_registration(self, 'User_2')
        TestSetUpData.user_login(self, 'User_2')
        response = self.client.get(get_user_actions_url(1))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)