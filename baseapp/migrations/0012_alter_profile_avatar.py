# Generated by Django 4.1.3 on 2022-12-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0011_profile_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default_header.png', upload_to='profile_images'),
        ),
    ]
