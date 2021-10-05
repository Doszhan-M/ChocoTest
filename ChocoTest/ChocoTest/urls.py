from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Choco API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='auth')),
    path('api/', schema_view),

    path('api/', include('Apps.Accounts.urls', namespace='Accounts')),
    path('api/', include('Apps.ToDo.urls', namespace='ToDo')),
]
