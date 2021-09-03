from django_filters import FilterSet, ModelChoiceFilter

from .models import Price
from ..products.models import Product


class PricesFilter(FilterSet):

    slug = ModelChoiceFilter(field_name="product_slug", queryset=Product.objects.all())

    class Meta:
        model = Price
        fields = ("product", )
