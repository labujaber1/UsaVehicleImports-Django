# Generated by Django 4.2.5 on 2023-11-06 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0046_navhtmlpage_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='navhtmlpage',
            old_name='header',
            new_name='title',
        ),
    ]