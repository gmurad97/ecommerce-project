# Generated by Django 5.1.6 on 2025-02-28 22:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_brand_created_at_alter_brand_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time of record creation (automatically).', verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='category',
            name='deleted_at',
            field=models.DateTimeField(blank=True, help_text='Date and time of soft deletion (automatically).', null=True, verbose_name='Deleted At'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(help_text='Image representing the category.', upload_to='category/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'svg', 'gif', 'webp', 'bmp', 'tiff'])], verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Category name.', max_length=255, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, help_text='Unique identifier for the category in the URL.', unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True, help_text='Category visibility status.', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date and time of the last update (automatically).', verbose_name='Updated At'),
        ),
    ]
