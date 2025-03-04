# Generated by Django 5.1.6 on 2025-03-04 01:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_brand_logo_alter_category_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(blank=True, help_text='Category logo image. Accepted formats: JPG, JPEG, PNG, SVG, GIF, WEBP, BMP, TIFF.', null=True, upload_to='category/image/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'svg', 'gif', 'webp', 'bmp', 'tiff'])], verbose_name='Image'),
        ),
    ]
