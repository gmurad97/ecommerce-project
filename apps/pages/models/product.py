from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField()

    slug = models.SlugField()

    description = models.TextField()
    brand = models.CharField()
    price = models.DecimalField()
    discount = models.DecimalField()
    image = models.ImageField()

    status = models.BooleanField()

    category = models.ForeignKey()

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()  # SOFT DELETE

    def __str__(self):
        return "name? + brand? + price?"

    def get_absolute_url(self):
        return "reversed link ^_^"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-created_at",)
