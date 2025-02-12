from django.urls import path
from .views import HomeView, PromotionListAPI, PromotionDetailAPI


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/promotions/', PromotionListAPI.as_view(), name='polls-list-api' ),
    path('api/promotion/<int:pk>', PromotionDetailAPI.as_view(), name='polls-detail-api'),
]