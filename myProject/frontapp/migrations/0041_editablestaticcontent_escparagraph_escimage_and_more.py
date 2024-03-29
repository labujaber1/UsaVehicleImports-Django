# Generated by Django 4.2.5 on 2023-11-04 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0040_previousexamplesimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditableStaticContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('HomeHero', 'HomeHero'), ('Home', 'Home'), ('Importing', 'Importing'), ('Sourcing', 'Sourcing'), ('Transportation', 'Transportation'), ('GalleryHero', 'GalleryHero'), ('GalleryBreaker', 'GalleryBreaker'), ('GalleryExamplePics', 'GalleryExamplePics'), ('NewsHero', 'NewsHero'), ('', ''), ('', '')], max_length=100)),
                ('slug', models.SlugField()),
                ('header', models.CharField(blank=True, max_length=100)),
                ('subHeader', models.CharField(blank=True, max_length=100)),
                ('badge', models.ImageField(height_field=50, upload_to='images/editableContent/', width_field=50)),
                ('shortDescription', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ESCParagraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField()),
                ('editableStaticContentFk', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='escToPara_fk', to='frontapp.editablestaticcontent')),
            ],
        ),
        migrations.CreateModel(
            name='ESCImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/editableContent/')),
                ('filename', models.CharField(blank=True, default='default.jpg', max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('editableStaticContentFk', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='escToImage_fk', to='frontapp.editablestaticcontent')),
            ],
        ),
        migrations.CreateModel(
            name='ESCExternalLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('externalLink', models.URLField(blank=True)),
                ('editableStaticContentFk', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='escToLink_fk', to='frontapp.editablestaticcontent')),
            ],
        ),
    ]
