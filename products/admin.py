from django.contrib import admin
from .models import *
# Register your models here.

class ProductImageInLine(admin.TabularInline):
    model = ProductImage

class ProductTypeAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductType._meta.fields]


    class Meta:
        model = ProductType

admin.site.register(ProductType, ProductTypeAdmin)

class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInLine]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)