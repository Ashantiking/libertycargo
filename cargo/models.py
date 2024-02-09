
from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from category.models import *
# Create your models here.


class Cargo(models.Model):
    cargoID = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, unique=True)
    category = models.ManyToManyField(Category, related_name='cargo_category')
    # ship_from = models.ManyToManyField(Country, related_name='ship_from')
    # ship_to = models.ManyToManyField(Country, related_name='ship_to')
    supplier_address = models.CharField(max_length=25)
    supplier_phone = models.CharField(max_length=25)
    supplier_email = models.EmailField(max_length=100)

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cargo')
