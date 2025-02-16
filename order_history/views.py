from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from django.http import JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Order, OrderItem
from cart.models import Cart, CartItem

# Create your views here.

class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "order_history/order_history.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-created_at")

class ReorderView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id, user=request.user)
        cart, created = Cart.objects.get_or_create(user=request.user)

        for item in order.order_items.all():
            cart_item, created = CartItem.objects.get_or_create(cart=cart, dish=item.dish)
            cart_item.quantity += item.quantity
            cart_item.save()

        return redirect("cart")