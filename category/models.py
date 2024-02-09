from django.db import models

from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    country = models.CharField(max_length=500, unique=True)
    city = models.CharField(max_length=500, unique=True)
    code = models.CharField(max_length=5, unique=True)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country
