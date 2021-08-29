from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..products.models import Product
from ..products.serializers import ProductSerializer


class ListUpdateDeleteViewSet(mixins.ListModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    pass


class FavouritesViewSet(ListUpdateDeleteViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        user = request.user
        products = user.favourites.objects.all()

        if products is not None:
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        request.user.favourites.objects.remove(product)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        request.user.favourites.objects.add(product)

        return Response(status=status.HTTP_200_OK)
