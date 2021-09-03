from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins

from .models import Price
from .serializers import PriceSerializer


class PricesViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ("product__slug", )
