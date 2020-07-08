from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'created', 'updated']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}

