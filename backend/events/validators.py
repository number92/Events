from datetime import date
from django.core.exceptions import ValidationError


def must_future_date(value):
    if value < date.today():
        raise ValidationError("The date cannot be in the past!")
