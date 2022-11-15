from django.contrib import admin
from .models import Category, PodCategories, Modeli_tovarov


class CategoryName(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'parents']


admin.site.register(Category, CategoryName)


class PodCategoriesName(admin.ModelAdmin):
    model = PodCategories
    list_display = ['name', 'parents']


admin.site.register(PodCategories, PodCategoriesName)
admin.site.register(Modeli_tovarov)
