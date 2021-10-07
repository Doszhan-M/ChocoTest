# Generated by Django 3.2.5 on 2021-10-07 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0005_alter_todo_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'Низкий'), (1, 'Нормальный'), (2, 'Высокий'), (3, 'Не присвоен')], default=1, null=True),
        ),
    ]
