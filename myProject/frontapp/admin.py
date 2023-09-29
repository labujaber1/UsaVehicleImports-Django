from django.contrib import admin
from .models import Vehicle, Images, GeneralEnquiry, Post

# Register your models here.


class ImageAdmin(admin.StackedInline):
    model = Images


@admin.register(Vehicle)
class ImagesAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]

    class Meta:
        model = Vehicle


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(GeneralEnquiry)
class GeneralEnquiryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class Post(admin.ModelAdmin):
    pass
