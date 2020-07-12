import datetime
from django.test import TestCase
from rest_framework import status
from tests.setupdata import TestSetUpData
from constants import LIKE_URL


class PostsTest(TestCase, TestSetUpData):

    def setUp(self):
        TestSetUpData.setUpData(self)

    def test_get_all_likes_count(self):
        date = datetime.date.today()
        [self.client.post(f'/{LIKE_URL}', {'post': x}) for x in ('1', '2', '3')]
        response = self.client.get(f'/api/v1/likescount/?date_from={date}&date_to={date}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        day = response.data['results'][0]['day']
        count = response.data['results'][0]['count']
        self.assertEqual(day, str(date))
        self.assertEqual(count, 3)
