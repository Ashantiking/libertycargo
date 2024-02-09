from django.contrib import admin
from .models import *
from category.models import *
# Register your models here.


class CargoAdmin(admin.ModelAdmin):
    #    list_display = ['name', 'cargoID']
    # form = SupplierForm
    #    list_filter = ['name']
    search_fields = ['cargoID', 'name', 'category']


admin.site.site_header = 'Liberty Administrator'
admin.site.register(Cargo, CargoAdmin)
