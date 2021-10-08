from django.db import connections
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsEmployeeUser, IsAdministratorUser

from .serializers import ToDoserializer
from .models import ToDo


class ToDoListApi(generics.ListAPIView):
    '''Просмотр всех задач'''
    serializer_class = ToDoserializer
    queryset = ToDo.objects.all()
    permission_classes = (IsAuthenticated,)


class ToDoCreateApi(generics.CreateAPIView):
    '''Создать задачу'''
    serializer_class = ToDoserializer
    permission_classes = (IsEmployeeUser,)

    def post(self, request, *args, **kwargs):
        try:
            if not request.data['deadline']:
                request.data['deadline'] = None
                
            if not request.data['priority']:
                request.data['priority'] = 3
        except KeyError:
            self.create(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)


class ToDoUpdateDelApi(generics.RetrieveUpdateDestroyAPIView):
    '''Обновить или удалить задачу'''
    serializer_class = ToDoserializer
    permission_classes = (IsAdministratorUser,)             

    def get_object(self):
        '''Получить обьект.'''
        data = self.request.data.get('data')
        object = ToDo.objects.get(id=data)
        return object

    def patch(self, request, *args, **kwargs):
        if not request.data['deadline']:
            request.data['deadline'] = None
        if not request.data['priority']:
            request.data['priority'] = 3
        return self.update(request, *args, **kwargs)

        
class IndexView(TemplateView):
    """Начальный шаблон для js"""
    template_name = 'index.html'
    

