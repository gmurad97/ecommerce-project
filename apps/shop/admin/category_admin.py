from django.contrib import admin
from django.templatetags.static import static
from django.utils.safestring import mark_safe
from ..models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("image_tag", "name", "slug_tag", "created_at_tag", "updated_at_tag", "status")
    list_display_links = ("name",)
    list_editable = ("status",)
    list_per_page = 10
    list_filter = ("status", "created_at", "updated_at", "deleted_at")
    search_fields = ("name",)
    readonly_fields = ("image_tag", "created_at", "updated_at", "deleted_at")
    exclude = ("slug",)
    fieldsets = (
        (
            "Main Settings",
            {
                "fields": (
                    "name",
                    "image",
                )
            },
        ),
        (
            "General Information",
            {
                "classes": ("collapse",),
                "fields": ("image_tag", "created_at", "updated_at", "deleted_at"),
            },
        ),
    )

    @admin.display(description="Slug")
    def slug_tag(self, obj):
        return mark_safe(f"<a class='slug__link' href='{obj.get_absolute_url()}'>🔗{obj.slug}</a>")

    @admin.display(description="Image")
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f"<a href='{obj.image.url}' data-lity><img class='preview__image' src='{obj.image.url}' alt='Preview'></a>"
            )
        else:
            return mark_safe(
                f"<a href='{static("admin/img/no_image.png")}' data-lity><img class='preview__image' src='{static("admin/img/no_image.png")}' alt='Preview'></a>"
            )

    @admin.display(description="Created At")
    def created_at_tag(self, obj):
        return mark_safe(f"<span class='created_at'>⏰{obj.created_at.strftime('%d-%m-%Y %H:%M:%S')}</span>")

    @admin.display(description="Updated At")
    def updated_at_tag(self, obj):
        return mark_safe(f"<span class='updated_at'>⏰{obj.updated_at.strftime('%d-%m-%Y %H:%M:%S')}</span>")

    class Media:
        css = {
            "all": (
                "admin/css/media_style.css",
                "admin/plugins/lity@2.4.1/lity.min.css",
            ),
        }

        js = ("admin/plugins/lity@2.4.1/lity.min.js",)
