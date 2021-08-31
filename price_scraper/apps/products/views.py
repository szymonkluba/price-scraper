from django.db.models import F
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Category, Product
from . import serializers


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return serializers.CategoryDetailSerializer
        return serializers.CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Product.objects.filter(pk=instance.id).update(popularity=F("popularity") + 1)
        serializer = self.get_serializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)