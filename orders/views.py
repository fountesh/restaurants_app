from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Order, OrderItem
from cart.models import Cart, CartItem
from .forms import OrderForm

# Create your views here.

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("order_list")

    def form_valid(self, form):
        order = form.save(commit=False)
        order.user = self.request.user
        order.save()

        # Додаємо страви з кошика до замовлення
        cart = get_object_or_404(Cart, user=self.request.user)
        for cart_item in cart.cart_items.all():
            OrderItem.objects.create(order=order, dish=cart_item.dish, quantity=cart_item.quantity)
        
        # Очищаємо кошик після оформлення замовлення
        cart.cart_items.all().delete()

        return super().form_valid(form)

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-created_at")

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/order_detail.html"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)