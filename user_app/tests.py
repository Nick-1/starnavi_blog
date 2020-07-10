from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
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

        login_url = reverse('jwt-login')
        user = self.client.post(login_url, {'username': 'sany', 'password': 'sany'}, format='json')
        token = user.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_get_actions(self):
        response = self.client.get('/api/v1/actions/user/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
