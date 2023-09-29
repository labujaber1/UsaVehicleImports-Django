# Generated by Django 4.2.5 on 2023-09-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0012_alter_images_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='filename',
            field=models.CharField(blank=True, default='images/inventory/default.jpg', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='images',
            field=models.ImageField(default='images/inventory/default.jpg', upload_to='images/inventory/'),
        ),
    ]
