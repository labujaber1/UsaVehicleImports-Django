# Generated by Django 4.2.5 on 2023-10-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0022_businessdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessdetails',
            name='address_town',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]