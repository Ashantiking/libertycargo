from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,  View
from django.utils import timezone
#from shopping_cart.models import Order
from .models import *
#from category.models import Category
#from .forms import ProductForm, CheckoutForm, EditForm
# Create your views here.



class CargoView(ListView):
    model = Cargo
    template_name = 'cargo/ship.html'
    paginate_by = 12
    ordering = ['-date_added']
    success_url = reverse_lazy('cargo')


# class orderSummaryView(DetailView):
#    model = Order
#    template_name = 'product/order_summary.html'


class CargoDetailView(DetailView):
    model = Cargo
    template_name = 'cargo/shop_detail.html'
    success_url = reverse_lazy('Cargo')

    def get_context_data(self, *args, **kwargs):
        #        cat_menu = Category.objects.all()
        context = super(CargoDetailView, self).get_context_data()

        #stuff = get_object_or_404(Cargo, id=self.kwargs['pk'])
        #total_likes = stuff.total_likes()
        #context["cat_menu"] = cat_menu
        #context["total_likes"] = total_likes
        return context



class NewCargoView(CreateView):
    model = Cargo
    #form_class = CargoForm
    template_name = 'cargo/new_cargo.html'
    #success_url = reverse_lazy('cargo')

# class AddCategoryView(CreateView):
    #model = Category
    #form_class = ProductForm
    #template_name = 'add_category.html'
    #fields = '__all__'


class UpdateCargoView(UpdateView):
    model = Cargo
    #form_class = EditForm
    template_name = 'cargo/update_cargo.html'
    success_url = reverse_lazy('cargo')
