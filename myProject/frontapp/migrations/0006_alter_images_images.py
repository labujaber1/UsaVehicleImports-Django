# Generated by Django 4.2.5 on 2023-09-29 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0005_alter_images_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='images',
            field=models.ImageField(default='images/inventory/default.jpg', height_field='url_height', upload_to='images/inventory/', width_field='url_height'),
        ),
    ]