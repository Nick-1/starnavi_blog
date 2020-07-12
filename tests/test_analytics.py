import datetime
from django.test import TestCase
from rest_framework import status
from tests.setupdata import TestSetUpData
from constants import LIKE_URL, LIKE_COUNT_URL


class PostsTest(TestCase, TestSetUpData):

    def setUp(self):
        TestSetUpData.setUpData(self)

    def test_analytics_likes_count(self):
        date = datetime.date.today()
        [self.client.post(f'/{LIKE_URL}', {'post': x}) for x in ('1', '2', '3')]
        response = self.client.get(f'/{LIKE_COUNT_URL}?date_from={date}&date_to={date}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        day = response.data['results'][0]['day']
        count = response.data['results'][0]['count']
        self.assertEqual(day, str(date))
        self.assertEqual(count, 3)

    def test_analytics_likes_permissions(self):
        self.client.post(f'/{LIKE_URL}', {'post': '1'})
        TestSetUpData.user_registration(self, 'user_3')
        TestSetUpData.user_login(self, 'user_3')
        date = datetime.date.today()
        response = self.client.get(f'/{LIKE_COUNT_URL}?date_from={date}&date_to={date}')
        self.assertEqual(response.data['count'], 0)
