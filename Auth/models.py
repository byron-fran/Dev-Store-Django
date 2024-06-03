from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        null=False,
        verbose_name="Email",
        name="email",
        blank=False,
        error_messages="Email is required",
        max_length=50
    )
    username = models.CharField(
        help_text="username must be unique",
        error_messages="Username is required",
        max_length=50,
        unique=True
    )
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    class Meta:
        db_table = "users"
