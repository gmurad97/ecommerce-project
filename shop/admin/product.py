from django.contrib import admin
from ..models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    def changelist_view(self, request, extra_context = None):
        self.model._meta.verbose_name_plural = self.model.objects.count()
        return super().changelist_view(request, extra_context)