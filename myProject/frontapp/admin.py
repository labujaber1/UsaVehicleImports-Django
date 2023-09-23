from django.contrib import admin
from .models import Vehicle
from .models import Images
from .models import GeneralEnquiry

# Register your models here.


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass


@admin.register(GeneralEnquiry)
class GeneralEnquiryAdmin(admin.ModelAdmin):
    pass
