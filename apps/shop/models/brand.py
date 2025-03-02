from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        verbose_name="Name",
        help_text="Brand name.",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=False,
        verbose_name="Slug",
        help_text="URL-friendly unique identifier.",
    )
    logo = models.ImageField(
        upload_to="brands/logo/",
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "svg", "gif", "webp", "bmp", "tiff"])],
        blank=True,
        null=True,
        verbose_name="Logo",
        help_text="Brand logo image. Accepted formats: JPG, JPEG, PNG, SVG, GIF, WEBP, BMP, TIFF.",
    )
    status = models.BooleanField(
        default=True,
        verbose_name="Status",
        help_text="Brand visibility status.",
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
        return reverse("shop:brand_products", kwargs={"slug_id": self.slug})

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ("-created_at",)
