# Generated by Django 5.0 on 2024-05-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_product_image_url_delete_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/'),
        ),
    ]