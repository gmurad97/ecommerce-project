from django.contrib import admin
from django.utils.safestring import mark_safe
from ..models import Setting


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ("str_tag",)
    list_display_links = ("str_tag",)
    list_per_page = 1
    readonly_fields = ("created_at", "updated_at", "deleted_at")
    fieldsets = (
        (
            "Main Settings",
            {
                "fields": (
                    (
                        "maintenance_mode",
                        "snow_mode",
                    ),
                    "email",
                    "phone",
                    "working_time",
                    "facebook",
                    "instagram",
                    "linkedin",
                    "twitter",
                )
            },
        ),
        (
            "General Information",
            {
                "classes": ("collapse",),
                "fields": ("created_at", "updated_at", "deleted_at"),
            },
        ),
    )

    def has_add_permission(self, request):
        return not Setting.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    @admin.display(description="Type")
    def str_tag(self, obj):
        return f"🛠️{obj.__str__()}🛠️"

    @admin.display(description="Created At")
    def created_at_tag(self, obj):
        return mark_safe(f"<span class='created_at'>⏰{obj.created_at.strftime('%d-%m-%Y %H:%M:%S')}</span>")

    @admin.display(description="Updated At")
    def updated_at_tag(self, obj):
        return mark_safe(f"<span class='updated_at'>⏰{obj.updated_at.strftime('%d-%m-%Y %H:%M:%S')}</span>")

    class Media:
        css = {
            "all": ("admin/css/media_style.css",),
        }
