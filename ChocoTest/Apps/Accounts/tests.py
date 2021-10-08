from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status


User = get_user_model()
client = APIClient()


class AccountTests(APITestCase):

    def setUp(self):
        User.objects.create(username='casper', email='casper@mail.ru',
                            password='password123', is_employee=True, is_administrator=False)


    def test_create_account(self):
        '''Проверить регистрацию пользователя'''

        url = ('/api/users/signup/')
        data_reg = {
            "user": {
                "username": 'username1',
                "email": 'casper@mail.ru1',
                "is_employee": '1',
                "is_administrator": '0',
                "password": 'password123'
            }
        }
        response_reg = client.post(url, data_reg, format='json')
        self.assertEqual(response_reg.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(email='casper@mail.ru1').username, 'username1')


    def test_invalid_create_account(self):
        '''Проверить неправильную регистрацию пользователя'''

        url = ('/api/users/signup/')
        data = {
            "user": {
                "username": 'username1',
                "email": 'casper@mail.ru',
                "is_employee": '1',
                "is_administrator": '0',
                "password": 'password123'
            }
        }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)


    def test_get_toke(self):
        '''Проверить получение токена'''
        casper = User.objects.get(username='casper')
        self.assertEqual(type(casper.token), str)