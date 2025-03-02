from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from .brand import Brand
from .category import Category


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="Name",
        help_text="Product name.",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=False,
        verbose_name="Slug",
        help_text="URL-friendly unique identifier.",
    )
    description = models.TextField(
        blank=False,
        null=False,
        verbose_name="Description",
        help_text="Detailed product description.",
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        related_name="products",
        blank=False,
        null=True,
        verbose_name="Brand",
        help_text="The brand this product belongs to.",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="products",
        blank=False,
        null=True,
        verbose_name="Category",
        help_text="The category this product belongs to.",
    )
    stock_quantity = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Stock quantity",
        help_text="The number of items available in stock.",
    )
    sku = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        help_text="Unique SKU identifier for the product.",
    )
    rating = models.IntegerField(
        choices=[
            (1, "1 star"),
            (2, "2 stars"),
            (3, "3 stars"),
            (4, "4 stars"),
            (5, "5 stars"),
        ],
        default=1,
        verbose_name="Rating",
        help_text="The product rating from 1 to 5 stars.",
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name="Price",
        help_text="The price of the product.",
    )
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
        blank=False,
        null=False,
        verbose_name="Discount",
        help_text="The discount percentage (0.00 to 100.00).",
    )
    image = models.ImageField(
        upload_to="products/%Y/%m/%d/",
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "svg", "gif", "webp", "bmp", "tiff"])],
        blank=True,
        null=True,
        verbose_name="Image",
        help_text="Product image. Accepted formats: JPG, JPEG, PNG, SVG, GIF, WEBP, BMP, TIFF.",
    )
    status = models.BooleanField(
        default=True,
        verbose_name="Status",
        help_text="Product visibility status.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="Date and time of record creation (automatically).",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
        help_text="Date and time of the last update (automatically).",
    )
    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Deleted At",
        help_text="Date and time of soft deletion (automatically).",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", kwargs={"slug_id": self.slug})

    def discounted_price(self):
        result = round(self.price - (self.price * (self.discount / 100)), 2)
        return int(result) if result % 1 == 0 else result

    def discount_formatted(self):
        return int(self.discount) if self.discount % 1 == 0 else self.discount

    def has_stock(self):
        return self.stock_quantity > 0

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-created_at",)
