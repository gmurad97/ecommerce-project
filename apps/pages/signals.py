from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Product, Category


@receiver(pre_save, sender=Category)
def set_slug_category(sender, instance, **kwargs):
    category_slug = slugify(instance.name)
    if not instance.slug or category_slug != instance.slug:
        instance.slug = category_slug


@receiver(pre_save, sender=Product)
def set_slug_product(sender, instance, **kwargs):
    product_slug = slugify(instance.name)
    if not instance.slug or product_slug != instance.slug:
        instance.slug = product_slug


@receiver(pre_delete, sender=Product)
def delete_image_product(sender, instance, **kwargs):
    if instance.image and instance.image.name != "resources/product_default.png":
        instance.image.delete(save=False)
