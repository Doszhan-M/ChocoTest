from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User


class StrictBooleanField(serializers.BooleanField):
    def from_native(self, value):
        if value in ('true', 't', 'True', '1'):
            return True
        if value in ('false', 'f', 'False', '0'):
            return False
        return None


class RegistrationSerializer(serializers.ModelSerializer):
    """ Сериализация регистрации пользователя. """
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True) # токен только на чтение.

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token', 'is_employee', 'is_administrator',]


    def validate(self, data):
        '''Валидация булевых полей.'''
        is_employee = data['is_employee']
        is_administrator = data['is_administrator']
        if is_employee and is_administrator in ('true', 't', 'True', '1'):
            is_employee = True
            return is_employee
        if is_employee and is_administrator in ('false', 'f', 'False', '0'):
            is_employee = False
            return is_employee
        return data


    def create(self, validated_data):
        '''Создать юзера через функцию в UserManager.'''
        user = User.objects.create_user(**validated_data)
        return user



class LoginSerializer(serializers.Serializer):
    """ Сериализация авторизации пользователя. """
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'Вы забыли ввести свой email.'
            )

        if password is None:
            raise serializers.ValidationError(
                'Введите пароль.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Такой пользователь не существует.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'Учетная запись не активна.'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):
    """ Ощуществляет сериализацию и десериализацию объектов User. """

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token',)
        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        """ Выполняет обновление User. """
        # удалить поле пароля из словаря
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance