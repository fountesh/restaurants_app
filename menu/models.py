from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва страви")
    description = models.TextField(verbose_name="Опис", blank=True, null=True)
    ingredients = models.TextField(verbose_name="Інгредієнти", blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to='dishes/', verbose_name="Фото страви", blank=True, null=True)
    available = models.BooleanField(default=True, verbose_name="Доступність")
    is_popular = models.BooleanField(default=False, verbose_name="Популярна страва")
    is_new = models.BooleanField(default=False, verbose_name="Нова пропозиція")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes', verbose_name="Категорія")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата створення")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="Дата оновлення")

    class Meta:
        verbose_name = "Страва"
        verbose_name_plural = "Страви"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name