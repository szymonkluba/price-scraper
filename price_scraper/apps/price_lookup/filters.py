from django_filters import CharFilter
from django_filters import filters
from django_filters import ModelChoiceFilter
from django_filters.rest_framework import FilterSet

from ..products.models import Product
from .models import Price


class PricesFilter(FilterSet):

    # product = ModelChoiceFilter(
    #     field_name="product__slug",
    #     to_field_name="slug",
    #     queryset=Product.objects.all()
    # )

    product = CharFilter(field_name='product__slug')

    class Meta:
        model = Price
        fields = ('product', )
