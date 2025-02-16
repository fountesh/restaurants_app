from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Category, Dish

# Create your views here.

class CategoryListView(ListView):
    model = Category
    template_name = "menu/category_list.html"
    context_object_name = "categories"


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "menu/category_form.html"
    fields = ['name', 'description']
    success_url = reverse_lazy('menu:category_list')


class DishListView(ListView):
    model = Dish
    template_name = "menu/dish_list.html"
    context_object_name = "dishes"

    def get_queryset(self):
        return Dish.objects.filter(category__id=self.kwargs['category_id'], available=True)


class DishDetailView(DetailView):
    model = Dish
    template_name = "menu/dish_detail.html"
    context_object_name = "dish"


class DishCreateView(CreateView):
    model = Dish
    template_name = "menu/dish_form.html"
    fields = ['name', 'description', 'ingredients', 'price', 'image', 'is_popular', 'is_new', 'available', 'category']
    success_url = reverse_lazy('menu:category_list')


class DishUpdateView(UpdateView):
    model = Dish
    template_name = "menu/dish_form.html"
    fields = ['name', 'description', 'ingredients', 'price', 'image', 'is_popular', 'is_new', 'available', 'category']
    success_url = reverse_lazy('menu:category_list')


class DishDeleteView(DeleteView):
    model = Dish
    template_name = "menu/dish_confirm_delete.html"
    success_url = reverse_lazy('menu:category_list')