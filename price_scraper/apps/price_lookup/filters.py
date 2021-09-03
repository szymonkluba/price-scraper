from django_filters import filters, ModelChoiceFilter, CharFilter
from django_filters.rest_framework import FilterSet

from .models import Price
from ..products.models import Product


class PricesFilter(FilterSet):

    # product = ModelChoiceFilter(
    #     field_name="product__slug",
    #     to_field_name="slug",
    #     queryset=Product.objects.all()
    # )

    product = CharFilter(field_name="product__slug")

    class Meta:
        model = Price
        fields = ("product", )
