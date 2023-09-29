from datetime import date
from django.db import models
from django.core.validators import FileExtensionValidator
import uuid
# Create your models here.


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
                                 allowed_extensions=['', 'MOV', 'avi', 'mp4', 'webm', 'mkv'])], null=True, blank=True)
    date_uploaded = models.DateField(default=date.today, null=True)

    def __str__(self):
        return self.name


class Images(models.Model):
    images = models.ImageField(
        default='/media/images/inventory/default.jpg', upload_to='images/inventory/', height_field=0,
        width_field=0)
    filename = models.CharField(
        max_length=100, null=True, blank=True)
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


class Post(models.Model):
    title = models.CharField(max_length=500)
    image = models.URLField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4,
                          unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
