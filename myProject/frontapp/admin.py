from django.contrib import admin
from .models import BusinessDetails, Comment, Vehicle, Images, GeneralEnquiry, Post, Testimonials
#from .models import *
from  django.contrib.auth.models  import  Group
# Register your models here.

# Remove groups from admin site
admin.site.unregister(Group)

# Vehicle images added at vehicle screen
class ImageAdmin(admin.StackedInline):
    model = Images
    extra = 0
    max_num = 10



@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
    list_display = ['name','availability','date_uploaded']
    class Meta:
        model = Vehicle


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['filename']
    readonly_fields = ('display_default_image',)

    def display_default_image(self, obj):
        default_image_obj = Images.objects.filter(
            filename='images/inventory/default.jpg').first()
        if default_image_obj and default_image_obj == obj:
            return default_image_obj.images.url
        else:
            return 'No default image found'

    display_default_image.short_description = 'Default Image'




class GeneralEnquiryAdmin(admin.ModelAdmin):
    title = ['subject','name','phone_number','email','enquiry','enquiry_date']
    search_fields = ['subject','name','phone_number','email','enquiry','enquiry_date']
    list_filter = ['enquiry_date']
    list_display = ['subject','name','enquiry_date']
    class Meta:
        model = GeneralEnquiry
   


class PostAdmin(admin.ModelAdmin):
    fields = [('title','author'),'body_taster','body','image_url','image_upload','video','likes']
    search_fields = ['title','author','image_upload','video','created']
    list_filter = ['created']
    list_display = ['title','body_taster','created','likes']
    class Meta:
        model = Post
  


class TestimonialsAdmin(admin.ModelAdmin):
    title = ['name','address','quote','rate']
    list_filter = ['rate']
    list_display = ['name','rate']
    class Meta:
        model = Testimonials


class CommentAdmin(admin.ModelAdmin):
    fields = [('name','active'),'body','reply']
    list_display = ('name', 'body', 'post', 'created_on', 'active','reply')
    list_filter = ('post','active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
                
admin.site.register(GeneralEnquiry,GeneralEnquiryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Testimonials,TestimonialsAdmin)
admin.site.register(Comment,CommentAdmin)
@admin.register(BusinessDetails)

class BusinessDetailsAdmin(admin.ModelAdmin):
    list_display = ['business_name','image_tag']
    class Meta:
        model = BusinessDetails
        
    

