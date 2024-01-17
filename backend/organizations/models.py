from django.db import models
from django.conf import settings


class Organization(models.Model):
    """Организация"""

    title = models.CharField(
        "Наименование", max_length=settings.STR_LEN, unique=True
    )
    description = models.TextField("Описание", blank=True, null=True)
    address = models.CharField(
        "Адрес", max_length=settings.STR_LEN, unique=True
    )
    postcode = models.PositiveIntegerField("Почтовый индекс")

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
        ordering = ["title", "address"]

    def __str__(self):
        return self.title
