# Generated by Django 4.1.3 on 2022-12-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0015_alter_message_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]