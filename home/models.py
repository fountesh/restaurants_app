from django.db import models

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва страви")
    description = models.TextField(verbose_name="Опис", blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to='dishes/', verbose_name="Фото страви", blank=True, null=True)
    is_popular = models.BooleanField(default=False, verbose_name="Популярна страва")
    is_new = models.BooleanField(default=False, verbose_name="Нова пропозиція")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата оновлення")

    class Meta:
        verbose_name = "Страва"
        verbose_name_plural = "Страви"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Promotion(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва акції")
    description = models.TextField(verbose_name="Опис", blank=True, null=True)
    start_date = models.DateField(verbose_name="Дата початку")
    end_date = models.DateField(verbose_name="Дата завершення")
    image = models.ImageField(upload_to='promotions/', verbose_name="Зображення акції", blank=True, null=True)
    active = models.BooleanField(default=True, verbose_name="Активна пропозиція")

    class Meta:
        verbose_name = "Пропозиція"
        verbose_name_plural = "Пропозиції"
        ordering = ["-start_date"]

    def __str__(self):
        return self.title