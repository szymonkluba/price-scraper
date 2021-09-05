from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

from .models import Price


class PriceSerializer(serializers.ModelSerializer):
    store = serializers.SlugRelatedField(read_only=True, slug_field='name')
    slug = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = Price
        fields = ['price', 'store', 'slug', 'available', 'timestamp']


class StorePricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['name', 'slug', 'url', 'category', 'price',
                  'timestamp', 'available', 'image_url', 'in_favs']

    name = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    in_favs = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse_lazy('product-detail', kwargs={'slug': obj.product.slug})

    def get_name(self, obj):
        return obj.product.name

    def get_slug(self, obj):
        return obj.product.slug

    def get_image_url(self, obj):
        return obj.product.image_url

    def get_in_favs(self, obj):
        request = self.context.get('request')
        if request:
            if request.user.is_authenticated and obj.product in request.user.favourites.all():
                return True
        return False

    def get_category(self, obj):
        return obj.product.category.name
