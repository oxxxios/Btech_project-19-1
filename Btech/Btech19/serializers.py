from rest_framework import serializers
from . import models
from .models import Product, Category, ImageProduct
from rest_framework.exceptions import ValidationError


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class ProductValidateSerializer(serializers.Serializer):
    image = serializers.ImageField()
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    cpu = serializers.CharField()
    main_camera = serializers.CharField()
    front_camera = serializers.CharField()
    memory = serializers.IntegerField()
    ram = serializers.IntegerField()
    is_hit = serializers.BooleanField()
    is_active = serializers.BooleanField()

    def validate_product(self, product):
        try:
            Product.objects.get(id=product)
        except Product.DoesNotExist:
            raise ValidationError('Product Not Fount')
        return product


class ImageValidateSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    image = serializers.ImageField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Category
        fields = '__all__'


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField()
    paret = serializers.IntegerField()

