# Generated by Django 4.2.5 on 2023-11-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0037_faqs'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalenquiry',
            name='replied',
            field=models.BooleanField(default=False),
        ),
    ]
