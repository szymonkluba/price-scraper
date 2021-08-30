from rest_framework import serializers

from .models import Product, Category
from ..price_lookup.serializers import PriceSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "popularity", "category", "current_prices"]

    current_prices = serializers.SerializerMethodField()

    def get_current_prices(self, obj):
        prices = obj.product_prices.order_by('timestamp').distinct('store')
        serializer = PriceSerializer(prices, many=True)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "products"]

    products = serializers.HyperlinkedIdentityField(view_name="products_list")
