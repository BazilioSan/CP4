# Generated by Django 5.1.4 on 2024-12-08 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(help_text='Введите тему письма', max_length=255, verbose_name='Тема письма')),
                ('body', models.TextField(help_text='Введите сообщение', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['head'],
            },
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Введите Email', max_length=254, unique=True, verbose_name='Email')),
                ('name', models.CharField(help_text='Введите Ф.И.О.', max_length=100, verbose_name='Фамилия Имя Отчество')),
                ('comment', models.TextField(blank=True, help_text='Введите комментарий', null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_first_shipment', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время начала рассылки')),
                ('date_of_end_shipment', models.DateTimeField(auto_now=True, verbose_name='Дата и время окончания рассылки')),
                ('status', models.CharField(choices=[('end', 'Завершена'), ('created', 'Создана'), ('start', 'Запущена')], default='created', verbose_name='Статус рассылки')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.message', verbose_name='Сообщение')),
                ('recipient', models.ManyToManyField(to='newsletter.recipient', verbose_name='Получатель')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'ordering': ['status'],
            },
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_attempt', models.DateTimeField(auto_now=True, verbose_name='Дата и время попытки рассылки')),
                ('status', models.CharField(choices=[('successful', 'Успешно'), ('not successful', 'Не успешно')], default='created', verbose_name='Статус попытки рассылки')),
                ('mail_server_response', models.TextField(verbose_name='Ответ почтового сервера')),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.newsletter', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
                'ordering': ['status'],
            },
        ),
    ]
