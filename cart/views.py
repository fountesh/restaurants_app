from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart, CartItem
from menu.models import Dish

# Create your views here.

class CartView(LoginRequiredMixin, TemplateView):
    template_name = "cart/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        context["cart"] = cart
        context["total_price"] = cart.total_price()
        return context

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, dish_id):
        dish = get_object_or_404(Dish, id=dish_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, dish=dish)
        cart_item.quantity += 1
        cart_item.save()
        return redirect("cart")

class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, dish_id):
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, dish_id=dish_id)
        cart_item.delete()
        return redirect("cart")

class UpdateCartItemView(LoginRequiredMixin, View):
    def post(self, request, dish_id):
        quantity = int(request.POST.get("quantity", 1))
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, dish_id=dish_id)
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        return redirect("cart")