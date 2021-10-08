import time
from django.utils import timezone
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from .models import ToDo
from Apps.Accounts.models import User


@shared_task
def deadline_alert(id):
    '''Уведомление на почту за час до дедлайна.'''
    todo = ToDo.objects.get(id=id)
    deadline = todo.deadline

    while (deadline - timezone.now()).seconds >= 3600:
        if (deadline - timezone.now()).seconds > 3600 * 24:
            time.sleep(3600 * 24)
        elif (deadline - timezone.now()).seconds > 3600 * 12:
            time.sleep(3600 * 4)
        elif (deadline - timezone.now()).seconds > 3600 * 2:
            time.sleep(3600)
        elif (deadline - timezone.now()).seconds > 3600:
            time.sleep(60)
            
    if (deadline - timezone.now()).seconds <= 3600:
        print(f'send {(deadline - timezone.now()).seconds} sec')
        # отправить форму по email всем пользователям
        html_content = render_to_string('alert_email.html',)
        array = User.objects.all()
        for user in array:
            msg = EmailMultiAlternatives(
                subject=f'Уведомление от ChocoTest',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()  # отсылаем
            time.sleep(30)
