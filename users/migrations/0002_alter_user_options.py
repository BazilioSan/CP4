# Generated by Django 5.1.4 on 2024-12-25 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "permissions": [("can_ban_user", "can ban user")],
                "verbose_name": ("Пользователь",),
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
