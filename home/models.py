from django.db import models

# Create your models here.

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