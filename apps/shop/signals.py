from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Brand, Category, Product


@receiver(pre_save, sender=Brand)
def set_slug_brand(sender, instance, **kwargs):
    brand_slug = slugify(instance.name)
    if not instance.slug or brand_slug != instance.slug:
        instance.slug = brand_slug


@receiver(pre_delete, sender=Brand)
def delete_image_brand(sender, instance, **kwargs):
    if instance.logo:
        instance.logo.delete(save=False)


@receiver(pre_save, sender=Brand)
def delete_old_logo_brand(sender, instance, **kwargs):
    if instance._state.adding and not instance.pk:
        return False
    try:
        old_logo = sender.objects.get(pk=instance.pk).logo
    except sender.DoesNotExist:
        return False
    if old_logo and old_logo != instance.logo:
        old_logo.delete(save=False)


@receiver(pre_save, sender=Category)
def set_slug_category(sender, instance, **kwargs):
    category_slug = slugify(instance.name)
    if not instance.slug or category_slug != instance.slug:
        instance.slug = category_slug


@receiver(pre_delete, sender=Category)
def delete_image_category(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


@receiver(pre_save, sender=Category)
def delete_old_image_category(sender, instance, **kwargs):
    if instance._state.adding and not instance.pk:
        return False
    try:
        old_image = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False
    if old_image and old_image != instance.image:
        old_image.delete(save=False)


@receiver(pre_save, sender=Product)
def set_slug_product(sender, instance, **kwargs):
    product_slug = slugify(instance.name)
    if not instance.slug or product_slug != instance.slug:
        instance.slug = product_slug


@receiver(pre_delete, sender=Product)
def delete_image_product(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


@receiver(pre_save, sender=Product)
def delete_old_image_product(sender, instance, **kwargs):
    if instance._state.adding and not instance.pk:
        return False
    try:
        old_image = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False
    if old_image and old_image != instance.image:
        old_image.delete(save=False)
