from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False, verbose_name="Name")
    slug = models.SlugField(unique=True, blank=True, null=False, verbose_name="Slug")
    logo = models.ImageField(
        upload_to="brands/",
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "svg", "gif", "webp", "bmp", "tiff"])],
        blank=False,
        null=False,
        verbose_name="Logo",
    )
    status = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="Deleted At")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:brand_products", kwargs={"slug_id": self.slug})

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ("-created_at",)
