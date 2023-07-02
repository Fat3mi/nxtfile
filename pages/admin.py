from django.contrib import admin
from .models import Book,category

# Register your models here.
@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display=['title']
    search_fields=['title']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['title','price','is_discount','price_with_discount','created','exist','cover_tag']
    list_filter=['author','is_discount','category','exist']
    ordering=['-created']
    search_fields=['title','description','author']