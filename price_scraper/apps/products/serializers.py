from rest_framework.serializers import ModelSerializer

from .models import Product, Category


class ProductSerializer(ModelSerializer):
    model = Product
    fields = ["name", "popularity", "category"]


class CategorySerializer(ModelSerializer):
    model = Category
    fields = ["name"]
