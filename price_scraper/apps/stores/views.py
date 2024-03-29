from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..price_lookup.models import Price
from ..price_lookup.serializers import StorePricesSerializer
from .models import Store
from .serializers import StoreSerializer


class StoreViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = 'slug'

    @action(detail=True)
    def products(self, request, *args, **kwargs):
        instance = self.get_object()
        prices = Price.objects.filter(store=instance).order_by(
            'product', '-timestamp').distinct('product')
        prices = self.paginate_queryset(prices)
        serializer = StorePricesSerializer(prices, many=True)

        return self.get_paginated_response(serializer.data)
