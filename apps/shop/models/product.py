from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from . import Brand, Category


class Product(models.Model):
    
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Name"
    )
    slug = models.SlugField(unique=True, blank=True, null=False, verbose_name="Slug")
    description = models.TextField(blank=False, null=False, verbose_name="Description")
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="products", verbose_name="Brand"
    )
    price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=False, null=False, verbose_name="Price"
    )
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        blank=False,
        null=False,
        verbose_name="Discount",
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )
    image = models.ImageField(
        upload_to="products/%Y/%m/%d/",
        default="resources/product_default.png",
        blank=True,
        null=False,
        verbose_name="Image",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Category",
    )
    status = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="Deleted At")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pages:product_detail", kwargs={"slug_id": self.slug})

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-created_at",)
