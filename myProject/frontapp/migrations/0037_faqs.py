# Generated by Django 4.2.5 on 2023-11-01 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0036_comment_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Importing', 'Importing'), ('Sourcing', 'Sourcing'), ('Transportation', 'Transportation'), ('Registration', 'Registration'), ('Car-Sales', 'Car-sales'), ('Other', 'Other')], max_length=50)),
                ('question', models.CharField(blank=True, max_length=250)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'FAQs',
            },
        ),
    ]
