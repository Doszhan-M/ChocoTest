from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

app_name = 'Accounts'
urlpatterns = [
    path('users/signup/', RegistrationAPIView.as_view()),
    path('users/signin/', LoginAPIView.as_view(),),
    path('user/update/', UserRetrieveUpdateAPIView.as_view()),
]
