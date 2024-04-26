# Generated by Django 5.0 on 2024-04-26 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages='Email is required', max_length=50, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages='Username is required', help_text='username must be unique', max_length=50, unique=True),
        ),
    ]
