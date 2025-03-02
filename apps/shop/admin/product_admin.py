from django.contrib import admin
from django.urls import reverse
from django.templatetags.static import static
from django.utils.safestring import mark_safe
from ..models import Brand, Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "image_tag",
        "name",
        "slug_tag",
        "brand_tag",
        "category_tag",
        "stock_quantity_tag",
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
        "brand",
        "category",
        "status",
        "created_at",
        "updated_at",
        "deleted_at",
    )
    search_fields = (
        "name",
        "brand",
        "category",
        "sku",
    )
    readonly_fields = (
        "image_tag",
        "created_at",
        "updated_at",
        "deleted_at",
    )
    exclude = ("slug",)
    fieldsets = (
        (
            "Main Settings",
            {
                "fields": (
                    "name",
                    "description",
                    "brand",
                    "category",
                    "stock_quantity",
                    "sku",
                    "rating",
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

    def has_add_permission(self, request):
        return Brand.objects.filter(status=True).exists() and Category.objects.filter(status=True).exists()

    @admin.display(description="Price")
    def price_tag(self, obj):
        return mark_safe(f"<span class='price'>${obj.discounted_price()}</span>")

    @admin.display(description="Discount")
    def discount_tag(self, obj):
        return mark_safe(f"<span class='discount'>{obj.discount_formatted()}%</span>")

    @admin.display(description="Stock Quantity")
    def stock_quantity_tag(self, obj):
        if obj.has_stock():
            return mark_safe(f"<span class='in_stock'>In Stock ({obj.stock_quantity})</span>")
        else:
            return mark_safe(f"<span class='out_of_stock'>Out Of Stock ({obj.stock_quantity})</span>")

    @admin.display(description="Slug")
    def slug_tag(self, obj):
        return mark_safe(f"<a href='{obj.get_absolute_url()}'>🔗{obj.slug}</a>")

    @admin.display(description="Brand")
    def brand_tag(self, obj):
        admin_change_url = reverse(
            "admin:%s_%s_change" % (obj.brand._meta.app_label, obj.brand._meta.model_name),
            args=[obj.brand.pk],
        )
        return mark_safe(f"<a href='{admin_change_url}'>🔰{obj.brand.name}</a>")

    @admin.display(description="Category")
    def category_tag(self, obj):
        admin_change_url = reverse(
            "admin:%s_%s_change" % (obj.category._meta.app_label, obj.category._meta.model_name), args=[obj.category.pk]
        )
        return mark_safe(f"<a href='{admin_change_url}'>📌{obj.category.name}</a>")

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
