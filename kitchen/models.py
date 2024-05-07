from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name", ]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(max_length=255)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

