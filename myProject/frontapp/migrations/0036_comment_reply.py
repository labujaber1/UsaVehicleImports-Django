# Generated by Django 4.2.5 on 2023-10-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0035_remove_comment_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
