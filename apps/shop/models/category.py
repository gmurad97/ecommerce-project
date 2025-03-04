from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        verbose_name="Name",
        help_text="Category name.",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=False,
        verbose_name="Slug",
        help_text="URL-friendly unique identifier.",
    )
    image = models.FileField(
        upload_to="category/image/",
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "svg", "gif", "webp", "bmp", "tiff"])],
        blank=True,
        null=True,
        verbose_name="Image",
        help_text="Category logo image. Accepted formats: JPG, JPEG, PNG, SVG, GIF, WEBP, BMP, TIFF.",
    )
    status = models.BooleanField(
        default=True,
        verbose_name="Status",
        help_text="Category visibility status.",
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
        return reverse("shop:category_products", kwargs={"slug_id": self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("-created_at",)
