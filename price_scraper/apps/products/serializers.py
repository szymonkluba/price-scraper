from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

from ..price_lookup.serializers import PriceSerializer
from .models import Category
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'url', 'popularity',
                  'category', 'category_link', 'current_prices', 'image_url']

    current_prices = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    category_link = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    def get_current_prices(self, obj):
        prices = obj.product_prices.order_by(
            'store', '-timestamp').distinct('store')
        serializer = PriceSerializer(prices, many=True)
        return serializer.data

    def get_url(self, obj):
        return reverse_lazy('product-detail', kwargs={'slug': obj.slug})

    def get_category_link(self, obj):
        return reverse_lazy('category-detail', kwargs={'slug': obj.category.slug})


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'products']

    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        return reverse_lazy('category-products', kwargs={'slug': obj.slug})


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'url']

    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse_lazy('category-detail', kwargs={'slug': obj.slug})
