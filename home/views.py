from django.shortcuts import render
from rest_framework import generics
from .serializers import PromotionSerializer
from django.views.generic import TemplateView, CreateView
from .models import Promotion
from menu.models import Dish

# Create your views here.

class HomeView(TemplateView):

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['popular_dishes'] = Dish.objects.filter(is_popular=True)[:5]
        context['active_promotions'] = Promotion.objects.filter(active=True)[:3]
        
        return context



class PromotionListAPI(generics.ListCreateAPIView ):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class PromotionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer