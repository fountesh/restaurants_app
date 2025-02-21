from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from menu.models import Dish

# Create your models here.

class Review(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", _("Очікує модерації")
        APPROVED = "approved", _("Схвалено")
        REJECTED = "rejected", _("Відхилено")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField(default=5, choices=[(i, i) for i in range(1, 6)], verbose_name="Оцінка")
    comment = models.TextField(verbose_name="Відгук")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.dish.name} ({self.rating}/5)"