# Generated by Django 4.2.5 on 2023-10-05 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0021_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(blank=True, max_length=100)),
                ('address_1stline', models.CharField(blank=True, max_length=100)),
                ('address_2ndline', models.CharField(blank=True, max_length=100)),
                ('address_county', models.CharField(blank=True, max_length=100)),
                ('address_postcode', models.CharField(blank=True, max_length=20)),
                ('contact_phone', models.CharField(blank=True, max_length=20)),
                ('contact_mobile', models.CharField(blank=True, max_length=20)),
                ('contact_email', models.EmailField(blank=True, max_length=100)),
                ('contact_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]