from rest_framework import viewsets

from price_scraper.apps.stores.models import Store
from price_scraper.apps.stores.serializers import StoreSerializer


class StoreViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer


