import jwt
from datetime import datetime, timedelta
from django.db import models
from django.conf import settings 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """"""
    def create_user(self, username, email, password=None, is_employee=False, is_administrator=False):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        print(is_employee)
        print(type(is_employee))

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.is_employee = is_employee
        user.is_administrator = is_administrator
        user.save()
        return user

    def create_superuser(self, username, email, password,):
        """ Создает и возвращает пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        """ Строковое представление модели"""
        return self.email

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
        
    @property
    def token(self):
        """Позволяет получить токен пользователя путем вызова user.token."""
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token