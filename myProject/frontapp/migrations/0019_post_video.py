# Generated by Django 4.2.5 on 2023-10-03 15:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0018_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['', 'MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
