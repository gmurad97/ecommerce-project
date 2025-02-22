from django.db import models


class Brand(models.Model):
    name = models.CharField(
        max_length=255, unique=True, blank=False, null=False, verbose_name="Name"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="Deleted At")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ("-created_at",)
