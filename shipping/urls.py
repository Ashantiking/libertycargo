

from django.urls import path
from django.views.generic.edit import UpdateView
from .views import *
from . import views


urlpatterns = [
    path('shipping/', ShippingView.as_view(), name='shipping'),
    path('shipping-detail/<int:pk>/',
         ShippingDetailView.as_view(), name='shipping-detail'),
    path('new_shipping/', NewShippingView.as_view(), name='new_shipping'),
    path('shipping-detail/edit/<int:pk>/',
         UpdateShippingView.as_view(), name='update_shipping'),
    path('search_shipping/', views.search_shipping, name='search_shipping'),
]
