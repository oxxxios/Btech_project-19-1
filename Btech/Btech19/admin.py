from django.contrib import admin
from .models import Product, Category, ImageProduct, Rating

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ImageProduct)
admin.site.register(Rating)