from .serializers import (
    ProductListSerializer,
    CategorySerializer,
    RatingSerializer
)
from .models import Product, Category
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = PageNumberPagination
    # permission_classes = [IsAuthenticated]


class ProductUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'id'


class CategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


@api_view(['POST'])
def rating(request, pk):
    serializer = RatingSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    serializer.get_or_create_product_rating(pk)
    return Response(request.data, status=status.HTTP_201_CREATED)

