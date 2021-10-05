from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.urls import reverse


class ToDo(models.Model):
    '''модель задачи'''

    class PriorityList(models.IntegerChoices):
        LOW = 1, ('Низкий')
        NORMAL = 2, ('Нормальный')
        HIGH = 3, ('Высокий')

    headline = models.CharField(max_length=200, blank=False, verbose_name='Заголовок',)
    description = models.TextField(blank=False, verbose_name='Описание',)
    priority = models.PositiveIntegerField(choices=PriorityList.choices, default=PriorityList.NORMAL, blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    def clean(self) -> None:
        deadline = self.deadline
        print(deadline)
        if deadline < timezone.now():
            raise ValidationError("The date cannot be in the past!")
        return deadline

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        '''Строковое отображение'''
        return f'{self.headline}'

    # def get_absolute_url(self):
    #     """получить ссылку на объект"""
    #     return reverse('todo')