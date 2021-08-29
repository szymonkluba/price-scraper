from rest_framework import serializers

from .models import Price


class PriceSerializer(serializers.ModelSerializer):
    model = Price
    fields = ['price', 'available', 'timestamp']