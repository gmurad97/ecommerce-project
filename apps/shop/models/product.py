from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Product(models.Model):
    descriptions = RichTextUploadingField(blank=True)
    images = models.JSONField(default=list)
