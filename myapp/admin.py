from django.contrib import admin
from .models import Product,Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Product, ProductAdmin)