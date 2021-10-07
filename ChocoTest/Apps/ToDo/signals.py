from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import ToDo
from django.conf import settings
from .tasks import deadline_alert
from django.utils import timezone



@receiver(post_save, sender=ToDo)
def create_deadline_alert(sender, instance, **kwargs):
    '''Создать уведомление на почту за час до дедлайна при создании модели'''

    if instance.deadline != None:
        id = instance.id
        deadline_alert.delay(id)

