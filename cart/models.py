from django.db import models
from django.conf import settings
from menu.models import Dish

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="cart", 
        verbose_name="Користувач"
    )
    dishes = models.ManyToManyField(
        Dish, 
        through="CartItem", 
        related_name="carts", 
        verbose_name="Страви"
    )

    def __str__(self):
        return f"Кошик користувача {self.user.username}"

    def total_price(self):
        """Обчислює загальну вартість кошика"""
        return sum(item.dish.price * item.quantity for item in self.cart_items.all())
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items", verbose_name="Кошик")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="cart_items", verbose_name="Страва")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість")

    def __str__(self):
        return f"{self.quantity}x {self.dish.name} у кошику {self.cart.user.username}"