from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Класс пользователей."""

    email = models.EmailField(
        "email",
        unique=True,
    )
    phone_number = PhoneNumberField("Номер телефона", region="RU", blank=True)
    username = models.CharField(
        "Пользователь", max_length=settings.STR_LEN, blank=True, null=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id", "email"]

    def __str__(self):
        return self.email
