from django.contrib import admin
from .models import Item, Order


@admin.register(Item)
class AmineItems(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    search_fields = ['name', 'price']

@admin.register(Order)
class AmineItems(admin.ModelAdmin):
    list_display = ['id','price']
    search_fields = ['id', 'price']

