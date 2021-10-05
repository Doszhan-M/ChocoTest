from django.urls import path

from .views import IndexView, ToDoListApi, ToDoCreateApi, ToDoUpdateDelApi


app_name = 'ToDo'

urlpatterns = [
    path('', IndexView.as_view()),

    path('todolist/', ToDoListApi.as_view(), name='todolist'),
    path('todocreate/', ToDoCreateApi.as_view(), name='todocreate'),
    path('todoupdel/', ToDoUpdateDelApi.as_view(), name='todo_update_del'),
]
