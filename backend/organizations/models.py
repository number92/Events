from django.db import models
from django.conf import settings

from users.models import User


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
    members = models.ManyToManyField(
        User,
        verbose_name="Участники",
        related_name="organization",
        through="Membership",
        through_fields=("organization", "user"),
        blank=True,
    )

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
        ordering = ["title", "address"]

    def __str__(self):
        return self.title


class Membership(models.Model):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, verbose_name="Организация"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Участник"
    )

    class Meta:
        verbose_name = "Участник организации"
        verbose_name_plural = "Участники организации"
        ordering = ["organization"]
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "user"],
                name="idx_unique_organization_user",
            )
        ]

    def __str__(self):
        return f"{self.organization.title}: {self.user.email}"
