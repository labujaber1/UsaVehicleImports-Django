from django.db import models

# Create your models here.


class Vehicle(models.Model):
    AVAIL_CHOICES = [('Y', 'Available'), ('N', 'Sold')]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, blank=True)
    availability = models.CharField(
        max_length=50, choices=AVAIL_CHOICES)
    price = models.PositiveIntegerField(
        default=0)
    description = models.CharField(max_length=500, blank=True)
    ImagesID = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return self.name


class Images(models.Model):
    images = models.ImageField(
        upload_to='images/inventory/', height_field=None, width_field=None, max_length=100)

    # def __str__(self):
    # return self.images


class GeneralEnquiry(models.Model):
    from_email = models.EmailField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    enquiry = models.TextField(max_length=500)

    def __str__(self):
        return self.name
