from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class CustomUserManager(BaseUserManager):
#     def create_user(self, phone, first_name, last_name, password, **extra_fields):
#         user = self.model(
#             phone=phone,
#             first_name=first_name,
#             last_name=last_name,
#             **extra_fields
#         )
#
#         user.set_password(password)
#
#         user.save()
#
#         return user
#
#     def create_superuser(self, username, phone, first_name, last_name, password, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser has to have is_staff being True")
#
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser has to have is_superuser being True")
#
#         return self.create_user(
#             username=username,
#             phone=phone,
#             first_name=first_name,
#             last_name=last_name,
#             password=password,
#             **extra_fields
#         )
class User(AbstractUser):
    username=models.CharField(max_length=100, unique=True)
    phone=models.CharField(max_length=13, unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = "first_name last_name".split()
    def __str__(self):
        return self.username