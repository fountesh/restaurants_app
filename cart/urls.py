from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView, UpdateCartItemView, GetCartTotalView

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("cart/add/<int:dish_id>/", AddToCartView.as_view(), name="add_to_cart"),
    path("cart/remove/<int:dish_id>/", RemoveFromCartView.as_view(), name="remove_from_cart"),
    path("cart/update/<int:dish_id>/", UpdateCartItemView.as_view(), name="update_cart_item"),
    path('cart/total/', GetCartTotalView.as_view(), name='get_cart_total'),
]