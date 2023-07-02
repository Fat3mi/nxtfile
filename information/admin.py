from django.contrib import admin
from .models import AboutUs,ContactUs
# Register your models here.

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display=['sitename','created','logo_tag']
    ordering=['-created']
    search_fields=['sitename']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=['user','created']
    list_filter=['created']
    ordering=['-created']
