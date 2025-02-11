from django.contrib import admin
from .models import Product,Cart, CartItem


admin.site.register(Cart)
admin.site.register(CartItem)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price', 'stock']
    search_fields=['name']


# Register your models here.


