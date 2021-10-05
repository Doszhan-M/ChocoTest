from django.db import models
from django.core.exceptions import ValidationError
import datetime

class ToDo(models.Model):
    '''модель задачи'''

    class PriorityList(models.IntegerChoices):
        LOW = 1, ('Низкий')
        NORMAL = 2, ('Нормальный')
        HIGH = 3, ('Высокий')

    headline = models.CharField(max_length=200, blank=False, verbose_name='Заголовок',)
    description = models.TextField(blank=False, verbose_name='Описание',)
    priority = models.PositiveIntegerField(choices=PriorityList.choices, default=PriorityList.NORMAL)
    deadline = models.DateTimeField(blank=False, default=datetime.datetime.now())

    def clean(self) -> None:
        deadline = self.deadline
        if deadline < datetime.datetime.now():
            raise ValidationError("The date cannot be in the past!")
        return deadline