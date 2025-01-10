from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Dish, Promotion

# Create your views here.

class HomeView(TemplateView):

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['popular_dishes'] = Dish.objects.filter(is_popular=True)[:5]
        context['active_promotions'] = Promotion.objects.filter(active=True)[:3]
        
        return context