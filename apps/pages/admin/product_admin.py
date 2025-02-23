from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from ..models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "image_tag",
        "name",
        "slug_tag",
        "brand_tag",
        "category_tag",
        "price_tag",
        "discount_tag",
        "created_at_tag",
        "updated_at_tag",
        "status",
    )
    list_display_links = ("name",)
    list_editable = ("status",)
    list_per_page = 10
    list_filter = (
        "name",
        "brand",
        "category",
        "price",
        "discount",
        "created_at",
        "updated_at",
        "status",
    )
    search_fields = ("name",)
    readonly_fields = ("image_tag", "created_at", "updated_at", "deleted_at")
    exclude = ("slug",)

    list_display = (
        "image_tag",
        "name",
        "slug_tag",
        "brand_tag",
        "category_tag",
        "price_tag",
        "discount_tag",
        "created_at_tag",
        "updated_at_tag",
        "status",
    )
    fieldsets = (
        (
            "Main Settings",
            {
                "fields": (
                    "name",
                    "brand",
                    "category",
                    "price",
                    "discount",
                    "image",
                    "status",
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

    @admin.display(description="Image")
    def image_tag(self, obj):
        return mark_safe(
            f"<a href='{obj.image.url}' data-lity><img class='preview__image' src='{obj.image.url}' alt='Preview'></a>"
        )

    @admin.display(description="Slug")
    def slug_tag(self, obj):
        return mark_safe(f"<a href='{obj.get_absolute_url()}'>🔗{obj.slug}</a>")

    def brand_tag(self, obj):
        admin_change_url = reverse(
            "admin:%s_%s_change"
            % (obj.brand._meta.app_label, obj.brand._meta.model_name),
            args=[obj.brand.pk],
        )
        return mark_safe(f"<a href='{admin_change_url}'>🔗{obj.brand.name}</a>")

    @admin.display(description="Category")
    def category_tag(self, obj):
        return mark_safe(
            f"<a href='{obj.category.get_absolute_url()}'>🔗{obj.category.name}</a>"
        )

    @admin.display(description="Price")
    def price_tag(self, obj):
        return mark_safe(f"<span class='price'>{obj.price}</span>")

    @admin.display(description="Discount")
    def discount_tag(self, obj):
        return mark_safe(f"<span class='discount'>{obj.discount}</span>")

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
            "all": ("admin/css/lity.min.css", "admin/css/style.css"),
        }
        js = ("admin/js/lity.min.js",)
