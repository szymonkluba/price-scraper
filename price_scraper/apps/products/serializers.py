from rest_framework import serializers

from .models import Product, Category
from ..price_lookup.serializers import PriceSerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["name", "popularity", "category", "current_prices"]

        current_prices = PriceSerializer(many=True, read_only=True)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name"]
