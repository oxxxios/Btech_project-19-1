from rest_framework import serializers
from . import models
from .models import Product, Category, ImageProduct, Rating
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


class RatingSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    rating = serializers.IntegerField(required=True, min_value=1, max_value=5)

    def get_or_create_product_rating(self, product_id: int):
        # для работоспособности
        obj, _ = Rating.objects.get_or_create(product=Product.objects.get(pk=product_id),
                                              user=self.get('user'))
        # для тестов
        # obj, _ = Rating.objects.get_or_create(product=Product.objects.first(),
        #                                       user=User.objects.first())
        obj.rating = self.data.get('rating', 1)
        obj.save()