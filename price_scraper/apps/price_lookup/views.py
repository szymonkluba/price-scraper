from rest_framework import viewsets, mixins, status

from .models import Price
from .serializers import PriceSerializer


class RetrieveListUpdateViewSet(mixins.RetrieveModelMixin,
                                mixins.ListModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    pass


class PricesViewSet(RetrieveListUpdateViewSet):

    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    