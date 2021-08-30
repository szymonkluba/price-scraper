from rest_framework import serializers

from .models import Price


class PriceSerializer(serializers.ModelSerializer):
    store = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Price
        fields = ['price', 'store', 'available', 'timestamp']
