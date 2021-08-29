from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    model = Product
    fields = ["name", "popularity", "category", "current_prices"]


class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = ["name"]
