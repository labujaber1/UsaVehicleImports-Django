# Generated by Django 4.2.5 on 2023-10-14 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0028_rename_from_email_generalenquiry_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalenquiry',
            name='enquiry_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
