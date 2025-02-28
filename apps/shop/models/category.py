from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False, verbose_name="Name")
    slug = models.SlugField(unique=True, blank=True, null=False, verbose_name="Slug")
    image = models.ImageField(
        upload_to="category/",
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "svg", "gif", "webp", "bmp", "tiff"])],
        blank=False,
        null=False,
        verbose_name="Image",
    )
    status = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="Deleted At")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:category_products", kwargs={"slug_id": self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("-created_at",)
