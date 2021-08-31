from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

from .models import Price


class PriceSerializer(serializers.ModelSerializer):
    store = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Price
        fields = ['price', 'store', 'available', 'timestamp']


class StorePricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['product', 'product_link', 'price', 'timestamp', 'available']

    product = serializers.SlugRelatedField(read_only=True, slug_field='name')
    product_link = serializers.SerializerMethodField()

    def get_product_link(self, obj):
        return reverse_lazy("product-detail", kwargs={"slug": obj.product.slug})
