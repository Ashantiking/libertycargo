
from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from category.models import *
from cargo.models import *
# Create your models here.


class Shipping(models.Model):
    track_number = models.CharField(max_length=20, unique=True)
    cargo = models.ManyToManyField(
        Cargo, related_name='cargo_name')
    category = models.ManyToManyField(
        Category, related_name='sipping_category')
    price = models.FloatField(default=7.00)
    hasArived = models.BooleanField(default=False)
    source_address = models.CharField(max_length=50)
    destination_address = models.CharField(max_length=50)
    sending_date = models.DateField()
    arrival_date = models.DateField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    sending_date = models.DateField()

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.track_number

    def get_absolute_url(self):
        return reverse('shipping')
