from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.utils import timezone

from .models import ToDo




class ToDoserializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True) #  только на чтение.

    class Meta:
        model = ToDo
        fields = ('headline', 'description', 'priority', 'deadline', 'id')

    def validate(self, data):
        if data['deadline'] != None:
            if data['deadline'] < timezone.now():
                raise serializers.ValidationError("Дедлайн не может быть в прошлом")
        return data
