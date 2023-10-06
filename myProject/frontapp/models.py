from datetime import date
from django.db import models
from django.core.validators import FileExtensionValidator
import uuid
from django.forms import ModelForm, Textarea


# Created models
class BusinessDetails(models.Model):
    business_name = models.CharField(max_length=100, blank=True)
    address_1stline = models.CharField(max_length=100, blank=True)
    address_2ndline = models.CharField(max_length=100, blank=True)
    address_town = models.CharField(max_length=100, blank=True)
    address_county = models.CharField(max_length=100, blank=True)
    address_postcode = models.CharField(max_length=20, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_mobile = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField(max_length=100, blank=True)
    contact_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.business_name


class Vehicle(models.Model):
    AVAIL_CHOICES = [('In-stock', 'Available'), ('No-stock', 'Sold')]
    TYPE_CHOICES = [('Car', 'Car'), ('Bike', 'Bike'), ('SUV', 'SUV'), ('Trailer', 'Trailer'),
                    ('Classic', 'Classic'), ('Other', 'Other')]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    availability = models.CharField(
        max_length=50, choices=AVAIL_CHOICES)
    price = models.PositiveIntegerField(
        default=0)
    description = models.CharField(max_length=500, blank=True)
    video = models.FileField(upload_to='video',
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['', 'MOV', 'avi', 'gif', 'mp4', 'webm', 'mkv'])], null=True, blank=True)
    date_uploaded = models.DateField(default=date.today, null=True)

    def __str__(self):
        return self.name


def default_image():
    return 'images/inventory/default.jpg'


class Images(models.Model):
    images = models.ImageField(
        default=default_image, upload_to='images/inventory/', height_field=0,
        width_field=0)
    filename = models.CharField(
        max_length=100, null=True, blank=True, default='default.jpg')
    vehicleFk = models.ForeignKey(
        Vehicle, related_name='vehicle_fk', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.images.url


class GeneralEnquiry(models.Model):
    from_email = models.EmailField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    enquiry = models.TextField(max_length=500)

    def __str__(self):
        return self.name


def default_post_image():
    return 'images/other/default_post_image.jpg'


class Post(models.Model):
    author = models.CharField(max_length=100, default='@UsaVehicleImports')
    title = models.CharField(max_length=500)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    image_upload = models.ImageField(
        default=default_post_image, upload_to='images/other/', height_field=0,
        width_field=0, null=True, blank=True)
    body = models.TextField()
    video = models.FileField(upload_to='video',
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['', 'MOV', 'avi', 'mp4', 'webm', 'mkv'])], null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4,
                          unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    quote = models.TextField()
    rate = models.PositiveIntegerField(
        default=0)

    def __str__(self):
        return self.name
