
from django.urls import path
from django.views.generic.edit import UpdateView
from .views import *

urlpatterns = [
    path('cargo/', CargoView.as_view(), name='cargo'),
    path('cargo-detail/<int:pk>/',
         CargoDetailView.as_view(), name='cargo-detail'),
    path('new_cargo/', NewCargoView.as_view(), name='new_cargo'),
    # path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('cargo-detail/edit/<int:pk>/',
         UpdateCargoView.as_view(), name='update_cargo'),
]
