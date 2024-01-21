from datetime import date
from django.db import models
from django.conf import settings
from organizations.models import Organization
from events.validators import must_future_date


class Event(models.Model):
    """Мероприятие"""

    title = models.CharField(
        "Наименование", max_length=settings.STR_LEN, unique=True
    )
    description = models.TextField("Описание", blank=True, null=True)
    organizations = models.ManyToManyField(
        Organization,
        related_name="events",
        verbose_name="Организации",
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Изображение", upload_to="images/", blank=True
    )
    date = models.DateField(
        "Дата", default=date.today, validators=[must_future_date]
    )

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ["title", "date"]

    def __str__(self):
        return self.title
