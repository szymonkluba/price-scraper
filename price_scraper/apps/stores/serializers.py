from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["name", "url", "store_prices"]

    store_prices = serializers.SerializerMethodField()

    def get_store_prices(self, obj):
        return reverse_lazy("store-products", kwargs={"slug": obj.slug})
