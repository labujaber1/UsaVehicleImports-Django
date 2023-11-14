# Generated by Django 4.2.5 on 2023-11-03 22:47

from django.db import migrations, models
import frontapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0039_generalenquiry_replied_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousExamplesImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default=frontapp.models.default_image, upload_to='images/gallery/')),
                ('filename', models.CharField(blank=True, default='default.jpg', max_length=100, null=True)),
                ('vehicleInfo', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'PreviousExamplesImages',
            },
        ),
    ]