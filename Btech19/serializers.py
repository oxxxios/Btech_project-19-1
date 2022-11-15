from rest_framework import serializers
from .models import Category, PodCategories, Modeli_tovarov


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PodCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = PodCategories
        fields = '__all__'


class ModeliTovarovSerializers(serializers.ModelSerializer):
    class Meta:
        model = Modeli_tovarov
        fields = '__all__'
