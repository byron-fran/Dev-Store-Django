# Generated by Django 5.0 on 2024-01-25 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_alter_product_image_alter_product_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
