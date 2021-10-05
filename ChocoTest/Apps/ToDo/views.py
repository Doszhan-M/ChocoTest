from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .serializers import ToDoserializer
from .models import ToDo


class IndexView(TemplateView):
    """Стартовая страница"""
    template_name = 'index.html'


class ToDoListApi(generics.ListAPIView):
    '''Просмотр всех задач'''
    serializer_class = ToDoserializer
    queryset = ToDo.objects.all()
    permission_classes = (IsAdminUser,)


class ToDoCreateApi(generics.CreateAPIView):
    '''Создать задачу'''
    serializer_class = ToDoserializer


class ToDoUpdateDelApi(generics.RetrieveUpdateDestroyAPIView):
    '''Обновить или удалить задачу'''
    serializer_class = ToDoserializer

    def get_object(self):
        data = self.request.data.get('data')
        print(data)
        object = ToDo.objects.get(headline=data)
        return object
    

