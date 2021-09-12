from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from ...products.models import Category
from ...products.models import Product
from ...products.views import CategoryViewSet


# noinspection DuplicatedCode
class CategoryViewsTests(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()

        self.category = Category(name='TestCategory')
        self.category.save()

        self.product = Product(name='TestProduct', category=self.category)
        self.product.save()

        self.category_detail = CategoryViewSet.as_view({'get': 'retrieve'})
        self.category_list = CategoryViewSet.as_view({'get': 'list'})
        self.category_products = CategoryViewSet.as_view({'get': 'products'})

        self.url = '/category/'

    def test_list(self) -> None:
        request = self.factory.get(self.url)
        response = self.category_list(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

        result = response.data['results'][0]

        self.assertEqual(result['name'], self.category.name)
        self.assertEqual(result['slug'], self.category.slug)

        products_url = reverse_lazy(
            'category-products', kwargs={'slug': self.category.slug})

        self.assertEqual(result['products'], products_url)

    def test_retrieve(self) -> None:
        request = self.factory.get(self.url)
        response = self.category_detail(request, slug=self.category.slug)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.category.name)
        self.assertEqual(response.data['slug'], self.category.slug)

        products_url = reverse_lazy(
            'category-products', kwargs={'slug': self.category.slug})

        self.assertEqual(response.data['products'], products_url)

    def test_category_products_list(self) -> None:
        request = self.factory.get(self.url)
        response = self.category_products(request, slug=self.category.slug)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

        result = response.data['results'][0]

        self.assertEqual(result['name'], self.product.name)
        self.assertEqual(result['slug'], self.product.slug)
