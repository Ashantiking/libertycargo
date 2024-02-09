
from django.contrib import admin
from .models import *
from category.models import *
# Register your models here.

# admin.site.register(Shipping)
# Register your models here.


class ShippingAdmin(admin.ModelAdmin):
    list_display = ['track_number', 'date_added']
    # form = SupplierForm
    list_filter = ['track_number']
    search_fields = ['track_number', 'category']


admin.site.register(Shipping, ShippingAdmin)
