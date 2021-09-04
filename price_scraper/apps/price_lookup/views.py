from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import viewsets

from .filters import PricesFilter
from .models import Price
from .serializers import PriceSerializer


class ListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class PricesViewSet(ListViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PricesFilter
