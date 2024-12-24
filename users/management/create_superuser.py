from django.core.management import BaseCommand

from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="admin@example.com")
        # user = User.objects.create_user(email="admin@example.com", password="123456")
        user.set_password("123")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

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
