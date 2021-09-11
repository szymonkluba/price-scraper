from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['name', 'slug', 'url', 'products']

    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        return reverse_lazy('store-products', kwargs={'slug': obj.slug})
