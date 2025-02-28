from django.contrib import admin
from django.utils.safestring import mark_safe
from ..models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at_tag", "updated_at_tag", "status")
    list_display_links = ("name",)
    list_editable = ("status",)
    list_per_page = 10
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at", "deleted_at")
    fieldsets = (
        ("Main Settings", {"fields": ("name",)}),
        (
            "General Information",
            {
                "classes": ("collapse",),
                "fields": ("created_at", "updated_at", "deleted_at"),
            },
        ),
    )

    @admin.display(description="Created At")
    def created_at_tag(self, obj):
        return mark_safe(
            f"<span class='created'>🕒{obj.created_at.strftime('%d-%m-%Y %H:%M:%S')}<span>"
        )

    @admin.display(description="Updated At")
    def updated_at_tag(self, obj):
        return mark_safe(
            f"<span class='updated'>🕒{obj.updated_at.strftime('%d-%m-%Y %H:%M:%S')}<span>"
        )

    class Media:
        css = {
            "all": ("admin/css/style.css",),
        }
