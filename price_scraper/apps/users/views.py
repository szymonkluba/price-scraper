from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..products.models import Product
from ..products.serializers import ProductSerializer


class ListAddDeleteViewSet(mixins.ListModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    pass


class FavouritesViewSet(ListAddDeleteViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ]
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):
        user = request.user
        products = user.favourites.all()

        if products is not None:
            products = self.paginate_queryset(products)
            serializer = self.get_serializer(products, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, slug=None, *args, **kwargs):
        if slug is not None:
            product = Product.objects.get(slug=slug)
            request.user.favourites.remove(product)

            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, slug=None, *args, **kwargs):
        if slug is not None:
            product = Product.objects.get(slug=slug)
            request.user.favourites.add(product)

            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
