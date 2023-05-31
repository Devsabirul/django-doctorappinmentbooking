from django.contrib.auth.models import AbstractUser
from jsonfield import JSONField
from django.db import models


class User(AbstractUser):
    is_admin = models.BooleanField(
        default=False,
        help_text="Designates that this user has permissions to access all dashboard.",
        verbose_name="Admin"
    )
    is_doctor = models.BooleanField(
        default=False,
        help_text="Designates that this user has permissions to access doctor dashboard.",
        verbose_name="Doctor"
    )
    is_patient = models.BooleanField(
        default=False,
        help_text="Designates that this user has permissions to access patient dashboard.",
        verbose_name="Patient"
    )
