# Generated by Django 3.2.5 on 2021-10-07 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0004_auto_20211005_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'Низкий'), (1, 'Нормальный'), (2, 'Высокий')], default=1, null=True),
        ),
    ]
