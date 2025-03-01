# Generated by Django 5.1.6 on 2025-02-28 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(help_text="Brand's official name.", max_length=255, unique=True, verbose_name='Name'),
        ),
    ]
