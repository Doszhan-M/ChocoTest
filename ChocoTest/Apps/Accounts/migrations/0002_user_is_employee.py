# Generated by Django 3.2.5 on 2021-10-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
    ]
