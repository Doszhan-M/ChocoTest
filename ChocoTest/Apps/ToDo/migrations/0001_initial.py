# Generated by Django 3.2.5 on 2021-10-05 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('priority', models.PositiveIntegerField(choices=[(1, 'Низкий'), (2, 'Нормальный'), (3, 'Высокий')], default=2)),
                ('deadline', models.DateTimeField(blank=True)),
            ],
        ),
    ]