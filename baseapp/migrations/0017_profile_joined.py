# Generated by Django 4.1.3 on 2022-12-21 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0016_alter_message_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='joined',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
