# Generated by Django 4.1.3 on 2022-12-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0008_remove_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default_avatar.jpg', upload_to='profile_images'),
        ),
    ]