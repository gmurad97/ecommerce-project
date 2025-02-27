from django.db import models


class Setting(models.Model):
    maintenance_mode = models.BooleanField(
        default=False, verbose_name="Maintenance Mode"
    )
    snow_mode = models.BooleanField(default=False, verbose_name="Snow Mode")
    email = models.EmailField(
        max_length=255, blank=True, null=True, verbose_name="Email"
    )
    phone = models.CharField(max_length=24, blank=True, null=True, verbose_name="Phone")
    facebook = models.URLField(blank=True, null=True, verbose_name="Facebook")
    instagram = models.URLField(blank=True, null=True, verbose_name="Instagram")
    linkedin = models.URLField(blank=True, null=True, verbose_name="Linkedin")
    twitter = models.URLField(blank=True, null=True, verbose_name="Twitter")
    working_time = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Working Time"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="Deleted At")

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"
