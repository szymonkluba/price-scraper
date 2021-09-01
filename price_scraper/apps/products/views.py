from django.db.models import F
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from .models import Category, Product


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return serializers.CategoryDetailSerializer
        return serializers.CategorySerializer

    @action(detail=True)
    def products(self, request, *args, **kwargs):
        instance = self.get_object()
        products = Product.objects.filter(category=instance)
        products = self.paginate_queryset(products)
        serializer = serializers.ProductSerializer(products, many=True)

        return self.get_paginated_response(serializer.data)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = "slug"
    filter_backends = [filters.SearchFilter]
    search_fields = ["@name"]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Product.objects.filter(pk=instance.id).update(popularity=F("popularity") + 1)
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
