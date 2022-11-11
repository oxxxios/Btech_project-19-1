from rest_framework import serializers
from . import models
from .models import Product, Category
from rest_framework.exceptions import ValidationError


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'category_name'.split()


class ProductListSerializers(serializers.ModelSerializer):
    category = CategorySerializers()

    class Meta:
        model = Product
        fields = 'id category image product_name installment price'.split()


class ProductItemSerializers(serializers.ModelSerializer):
    category = CategorySerializers()

    class Meta:
        model = Product
        fields = '__all__'