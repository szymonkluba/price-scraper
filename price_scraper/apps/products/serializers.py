from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

from .models import Product, Category
from ..price_lookup.serializers import PriceSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "popularity", "category", "current_prices"]

    current_prices = serializers.SerializerMethodField()

    def get_current_prices(self, obj):
        prices = obj.product_prices.order_by("store", "-timestamp").distinct("store")
        serializer = PriceSerializer(prices, many=True)
        return serializer.data


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "products"]

    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        return reverse_lazy("category-products", kwargs={"slug": obj.slug})


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "url"]

    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse_lazy("category-detail", kwargs={"slug": obj.slug})
