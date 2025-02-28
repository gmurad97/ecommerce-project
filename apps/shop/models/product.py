from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from .brand import Brand
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Name")
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=False, verbose_name="Slug")
    description = models.TextField(blank=False, null=False, verbose_name="Description")
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, related_name="products", blank=False, null=True, verbose_name="Brand"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="products", blank=False, null=True, verbose_name="Category"
    )
    stock_quantity = models.IntegerField()
    sku = models.CharField(max_length=100, unique=True,help_text="SKU INDENTIFIER")


    RATING_CHOICES = [
        (1, "1 star"),
        (2, "2 stars"),
        (3, "3 stars"),
        (4, "4 stars"),
        (5, "5 stars"),
    ]

    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
        verbose_name="Rating",
    )

    price = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False, verbose_name="Price")
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
        blank=False,
        null=False,
        verbose_name="Discount",
    )
    image = models.ImageField(
        upload_to="products/%Y/%m/%d/",
        blank=False,
        null=False,
        default="resource/product_default.png",
        verbose_name="Image",
    )
    status = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="Deleted At")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", kwargs={"slug_id": self.slug})
    
    def discount_normalize():
        pass # where 12.45 => 12.45 where 12.00 => 12
    
    def discounted_price():
        pass


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-created_at",)
