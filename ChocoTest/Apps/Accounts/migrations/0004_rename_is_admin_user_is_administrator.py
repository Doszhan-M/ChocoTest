# Generated by Django 3.2.5 on 2021-10-06 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_user_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_administrator',
        ),
    ]