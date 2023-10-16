# Generated by Django 4.2.5 on 2023-10-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0029_generalenquiry_enquiry_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businessdetails',
            options={'verbose_name_plural': 'Business Details'},
        ),
        migrations.AlterModelOptions(
            name='generalenquiry',
            options={'verbose_name_plural': 'General Enquiries'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='testimonials',
            options={'verbose_name_plural': 'Testimonials'},
        ),
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name_plural': 'Vehicles'},
        ),
        migrations.AddField(
            model_name='businessdetails',
            name='business_logo',
            field=models.ImageField(null=True, upload_to='images/other/'),
        ),
    ]
