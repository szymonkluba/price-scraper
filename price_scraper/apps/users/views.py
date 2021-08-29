from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from ..products.serializers import ProductSerializer
from .models import CustomUser


class ListUpdateDeleteViewSet(mixins.ListModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    pass


class FavouritesViewSet(ListUpdateDeleteViewSet):

    queryset = CustomUser.favourites.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        request.user.favourites.objects.remove(product)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        request.user.favourites.objects.add(product)
        return Response(status=status.HTTP_200_OK)