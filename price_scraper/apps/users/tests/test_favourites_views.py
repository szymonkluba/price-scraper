from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate

from ...products.models import Category
from ...products.models import Product
from ...users.models import CustomUser
from ...users.views import FavouritesViewSet


class FavouritesViewsTests(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()

        self.user = CustomUser.objects.create_user(
            email='test@example.com', password='Secret123')
        self.category = Category.objects.create(name='TestCategory')
        self.product = Product(name='TestProduct', category=self.category)
        self.product.save()

        self.favourites = FavouritesViewSet.as_view({
            'get': 'list',
            'post': 'create',
            'delete': 'destroy',
        })

        self.url = '/favourites/'

    def test_require_login_for_favourites(self) -> None:
        request = self.factory.get(self.url)
        response = self.favourites(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_add_to_favourites(self):
        request = self.factory.post(self.url, data={'slug': self.product.slug})
        force_authenticate(request, user=self.user)
        response = self.favourites(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.product, self.user.favourites.all())

    def test_remove_from_favourites(self):
        self.user.favourites.add(self.product)

        request = self.factory.delete(self.url)
        force_authenticate(request, user=self.user)
        response = self.favourites(request, slug=self.product.slug)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn(self.product, self.user.favourites.all())

    def test_list_favourites(self):
        self.user.favourites.add(self.product)

        request = self.factory.get(self.url)
        force_authenticate(request, user=self.user)
        response = self.favourites(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

        result = response.data['results'][0]

        self.assertEqual(result, {
            'name': self.product.name,
            'slug': self.product.slug,
            'url': reverse_lazy('product-detail', kwargs={'slug': self.product.slug}),
            'popularity': 0,
            'category': self.category.name,
            'category_link': reverse_lazy('category-detail', kwargs={'slug': self.category.slug}),
            'current_prices': [],
            'image_url': None,
            'in_favs': True
        })
