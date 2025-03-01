from django.db import models


class Setting(models.Model):
    maintenance_mode = models.BooleanField(
        default=False,
        verbose_name="Maintenance Mode",
        help_text="Turns on/off maintenance mode.",
    )
    snow_mode = models.BooleanField(
        default=False,
        verbose_name="Snow Mode",
        help_text="Turns on/off snow effect.",
    )
    email = models.EmailField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Email",
        help_text="Contact email address.",
    )
    phone = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        verbose_name="Phone",
        help_text="Contact phone number.",
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Address",
        help_text="Business address.",
    )
    working_time = models.TextField(
        blank=True,
        null=True,
        verbose_name="Working Time",
        help_text="Business working hours.",
    )
    facebook = models.URLField(
        blank=True,
        null=True,
        verbose_name="Facebook",
        help_text="Link to the Facebook page.",
    )
    instagram = models.URLField(
        blank=True,
        null=True,
        verbose_name="Instagram",
        help_text="Link to the Instagram page.",
    )
    linkedin = models.URLField(
        blank=True,
        null=True,
        verbose_name="LinkedIn",
        help_text="Link to the LinkedIn profile.",
    )
    twitter = models.URLField(
        blank=True,
        null=True,
        verbose_name="Twitter",
        help_text="Link to the Twitter profile.",
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
        return "Site Settings"

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"
        ordering = ("-created_at",)
