from django.test import TestCase
from rest_framework import status
from tests.setupdata import TestSetUpData
from constants import get_user_actions_url


class PostsTest(TestCase, TestSetUpData):

    def setUp(self):
        TestSetUpData.setUpData(self)

    def test_get_actions(self):
        response = self.client.get(get_user_actions_url(1))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
