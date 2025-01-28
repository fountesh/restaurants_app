from django.urls import path
from .views import CategoryListView, CategoryCreateView, DishListView, DishDetailView, DishCreateView, DishUpdateView, DishDeleteView

app_name = 'menu'

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:category_id>/', DishListView.as_view(), name='dish_list'),
    path('dish/<int:pk>/', DishDetailView.as_view(), name='dish_detail'),
    path('dish/create/', DishCreateView.as_view(), name='dish_create'),
    path('dish/<int:pk>/update/', DishUpdateView.as_view(), name='dish_update'),
    path('dish/<int:pk>/delete/', DishDeleteView.as_view(), name='dish_delete'),
]