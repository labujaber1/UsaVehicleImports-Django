from django.contrib import admin
#from .models import BusinessDetails, Vehicle, Images, GeneralEnquiry, Post, Testimonials
from .models import *
# Register your models here.



# Vehicle images added at vehicle screen
class ImageAdmin(admin.StackedInline):
    model = Images
    extra = 0
    max_num = 10


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]

    class Meta:
        model = Vehicle


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('display_default_image',)

    def display_default_image(self, obj):
        default_image_obj = Images.objects.filter(
            filename='images/inventory/default.jpg').first()
        if default_image_obj and default_image_obj == obj:
            return default_image_obj.images.url
        else:
            return 'No default image found'

    display_default_image.short_description = 'Default Image'



@admin.register(GeneralEnquiry)
class GeneralEnquiryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    pass


@admin.register(BusinessDetails)
class BusinessDetailsAdmin(admin.ModelAdmin):
    pass
