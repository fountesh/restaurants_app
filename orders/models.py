from django.db import models
from django.conf import settings
from menu.models import Dish
from users.models import CustomUser

# Create your models here.

class Order(models.Model):
    PAYMENT_METHODS = [
        ("cash", "Готівка"),
        ("card", "Картка"),
    ]

    STATUS_CHOICES = [
        ("pending", "Очікується"),
        ("confirmed", "Підтверджено"),
        ("preparing", "Готується"),
        ("delivering", "Доставляється"),
        ("completed", "Виконано"),
        ("canceled", "Скасовано"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="Користувач"
    )
    phone_number = models.CharField(max_length=10, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адреса доставки")
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHODS,
        default="cash",
        verbose_name="Спосіб оплати"
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default="pending",
        verbose_name="Статус замовлення"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def __str__(self):
        return f"Замовлення {self.id} - {self.user.username} ({self.get_status_display()})"

    def total_price(self):
        return sum(item.dish.price * item.quantity for item in self.order_items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name="Замовлення"
    )
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        verbose_name="Страва"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість")

    def __str__(self):
        return f"{self.quantity}x {self.dish.name} у замовленні {self.order.id}"