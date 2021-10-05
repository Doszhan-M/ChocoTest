from django.urls import path

from .views import IndexView


app_name = 'ToDo'


urlpatterns = [
    path('', IndexView.as_view()),
]
