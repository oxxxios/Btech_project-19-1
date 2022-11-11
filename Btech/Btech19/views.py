from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductListSerializers, ProductItemSerializers


class ProductsListAPIView(ListCreateAPIView):
    """List and Create Directors (example of a commentary)."""
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    pagination_class = PageNumberPagination


class ProductsItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductItemSerializers
    lookup_field = "id"
