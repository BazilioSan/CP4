from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager
from django.db import models


# class UserManager(DefaultUserManager):
#     def create_superuser(self, email, password=None, **extra_fields):
#         """
#         Создает и возвращает суперпользователя с заданным email и паролем.
#         """
#         if not email:
#             raise ValueError("Суперпользователь должен иметь адрес электронной почты.")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(
        max_length=11,
        verbose_name="Номер телефона",
        blank=True,
        null=True,
        help_text="Введите номер телефона (необязательно)",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        help_text="Загрузите свой аватар",
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Страна",
        blank=True,
        null=True,
        help_text="Укажите вашу страну",
    )
    token = models.CharField(max_length=100, blank=True, null=True, verbose_name="Токен пользователя")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # objects = UserManager()

    class Meta:
        verbose_name = ("Пользователь",)
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
