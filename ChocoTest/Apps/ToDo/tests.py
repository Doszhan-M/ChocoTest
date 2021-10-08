from django.test import TestCase
from django.contrib.auth import get_user_model
from Apps.ToDo.models import ToDo
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from Apps.ToDo.views import ToDoListApi


User = get_user_model()

class ToDoTest_db(TestCase):
    """ Test module for ToDo Api """

    def setUp(self):
        self.is_simple_user = User.objects.create(username='casper1', email='casper1@mail.ru',
                            password='password123', is_employee=False, is_administrator=False)
        self.is_employee = User.objects.create(username='casper2', email='casper2@mail.ru',
                            password='password123', is_employee=True, is_administrator=False)
        self.is_administrator = User.objects.create(username='casper3', email='casper3@mail.ru',
                            password='password123', is_employee=False, is_administrator=True)
        ToDo.objects.create(headline='Task1', description='description for task1',
                                   priority=1, deadline='2021-10-08 08:26:33.441939+00:00')
        ToDo.objects.create(headline='Task2', description='description for task2',
                                   priority=0, deadline='2021-11-08 08:26:33.441939+00:00')


    def test_todo_list(self):
        '''Получить список todo.'''
        client = APIClient()
        user = self.is_simple_user
        client.credentials(HTTP_AUTHORIZATION='Token ' + user.token)
        request = client.get('/api/todolist/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request.data), 2)


    def test_todo_list_non_user(self):
        '''Получить список todo без авторизации.'''
        client = APIClient()
        request = client.get('/api/todolist/')
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)


    def test_create(self):
        '''Создать todo.'''
        client = APIClient()
        user = self.is_employee
        client.credentials(HTTP_AUTHORIZATION='Token ' + user.token)
        body = {
            "headline": "Task3",
            "description": "description for task3",
            "priority": "1",
            "deadline": "2021-10-15T12:19:50"
        }
        request = client.post('/api/todocreate/', body)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)


    def test_create_option1(self):
        '''Создать todo без заголовка.'''
        client = APIClient()
        user = self.is_employee
        client.credentials(HTTP_AUTHORIZATION='Token ' + user.token)
        body = {
            "headline": "",
            "description": "description for task3",
            "priority": "1",
            "deadline": "2021-10-15T12:19:50"
        }
        request = client.post('/api/todocreate/', body)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_option2(self):
        '''Создать todo без дедлайна и приоритета.'''
        client = APIClient()
        user = self.is_employee
        client.credentials(HTTP_AUTHORIZATION='Token ' + user.token)
        body = {
            "headline": "Task4",
            "description": "description for task4",
            "priority": "",
            "deadline": ""
        }
        request = client.post('/api/todocreate/', body)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)


    def test_delete_todo(self):
        '''Удалить ToDO.'''
        self.assertEqual(len(ToDo.objects.all()), 2)
        client = APIClient()
        user = self.is_administrator
        client.credentials(HTTP_AUTHORIZATION='Token ' + user.token)
        id = ToDo.objects.get(headline='Task2').id
        body = {
            "data": id
        }
        request = client.delete('/api/todoupdel/', body)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(ToDo.objects.all()), 1)


    def test_update_todo(self):
        '''Изменить ToDO.'''
        self.assertEqual(ToDo.objects.get(headline='Task1').description, 'description for task1')
        client = APIClient()
        user = self.is_administrator
        client.credentials(HTTP_AUTHORIZATION='Token ' + user.token)
        id = ToDo.objects.get(headline='Task1').id
        body = {
            "data": id,
            "headline": "Task1",
            "description": "change description for task4",
            "priority": "",
            "deadline": ""
        }
        request = client.patch('/api/todoupdel/', body)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(ToDo.objects.get(headline='Task1').description, 'change description for task4')


    def test_update_todo(self):
        '''is_employee не могут изменять ToDO.'''
        client = APIClient()
        user = self.is_employee
        client.credentials(HTTP_AUTHORIZATION='Token ' + user.token)
        id = ToDo.objects.get(headline='Task1').id
        body = {
            "data": id,
            "headline": "Task1",
            "description": "change description for task4",
            "priority": "",
            "deadline": ""
        }
        request = client.patch('/api/todoupdel/', body)
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)