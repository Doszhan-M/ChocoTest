from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsEmployeeUser, IsAdministratorUser

from .serializers import ToDoserializer
from .models import ToDo


class IndexView(TemplateView):
    """Начальный шаблон для js"""
    template_name = 'index.html'


class ToDoListApi(generics.ListAPIView):
    '''Просмотр всех задач'''
    serializer_class = ToDoserializer
    queryset = ToDo.objects.all()
    permission_classes = (IsAuthenticated,)


class ToDoCreateApi(generics.CreateAPIView):
    '''Создать задачу'''
    serializer_class = ToDoserializer
    permission_classes = (IsEmployeeUser,)

    
class ToDoUpdateDelApi(generics.RetrieveUpdateDestroyAPIView):
    '''Обновить или удалить задачу'''
    serializer_class = ToDoserializer
    permission_classes = (IsAdministratorUser,)

    def get_object(self):
        '''Получить обьект.'''
        data = self.request.data.get('data')
        object = ToDo.objects.get(headline=data)
        return object
    

