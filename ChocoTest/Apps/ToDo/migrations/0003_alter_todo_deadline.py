# Generated by Django 3.2.5 on 2021-10-05 14:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0002_alter_todo_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 5, 14, 52, 30, 502342, tzinfo=utc)),
        ),
    ]