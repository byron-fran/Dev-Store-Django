# Generated by Django 5.0.6 on 2024-08-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_productimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.FileField(blank=True, upload_to='products/'),
        ),
    ]