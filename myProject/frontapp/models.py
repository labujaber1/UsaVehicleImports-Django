from datetime import date
from django.db import models
from django.core.validators import FileExtensionValidator
import uuid
from django.forms import ModelForm, Textarea
from django.utils.safestring import mark_safe

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
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    linkedIn = models.URLField(max_length=200, blank=True)
    google_map_link = models.CharField(max_length=300,blank=True)
    business_logo =  models.ImageField(upload_to='images/other/', null=True)  
    
    ##add logo to admin page
    def  image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="50" />' % (self.business_logo))
    image_tag.allow_tags = True 
    
    class  Meta:  
        verbose_name_plural  =  "Business Details" 
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
    class  Meta:  
            verbose_name_plural  =  "Vehicles"
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
    class  Meta:  
        verbose_name_plural  =  "Images"
    def __str__(self):
        return self.images.url


class GeneralEnquiry(models.Model):
    email = models.EmailField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    enquiry = models.TextField(max_length=500)
    enquiry_date = models.DateTimeField(auto_now_add=True)
    class  Meta:  
        verbose_name_plural  =  "General Enquiries"
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
    body_taster = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    video = models.FileField(upload_to='video',
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['', 'MOV', 'avi', 'mp4', 'webm', 'mkv'])], null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4,
                          unique=True, primary_key=True, editable=False)
    likes = models.PositiveIntegerField(default=0)
    
    class  Meta:  
        verbose_name_plural  =  "Posts"
    
    def __str__(self):
        return self.title
    
    @property
    def comment_count_true(self):
        comment_count = self.comments.filter(active=True).count()
        return comment_count

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    reply = models.CharField(max_length=200,blank=True)

    class Meta:
        ordering = ['created_on']
        
    def __str__(self):
        return 'Comment {} status {}'.format(self.name, self.active)
    
    
class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    quote = models.TextField()
    rate = models.PositiveIntegerField(
        default=0)
    class  Meta:  
        verbose_name_plural  =  "Testimonials"
    def __str__(self):
        return self.name



class Faqs(models.Model):
    CATEGORY_CHOICES=[('Importing', 'Importing'), ('Sourcing', 'Sourcing'),('Transportation','Transportation'),('Registration','Registration'),('Car-Sales','Car-sales'),('Other','Other')]
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES,blank=True)
    question = models.CharField(
        max_length=250,blank=True)
    answer = models.TextField()
    
    class  Meta:  
        verbose_name_plural  =  "FAQs"
    def __str__(self):
        return self.category  
    
