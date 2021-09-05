from apps.price_lookup.models import Price
from apps.products.models import Category
from apps.products.models import Product
from apps.stores.models import Store
from apps.stores.views import StoreViewSet
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase


class StoresViewsTest(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()

        self.store = Store(name='TestStore', url='https://www.test.com')
        self.store.save()

        category = Category.objects.create(name='TestCategory')

        self.product = Product(name='TestProduct', category=category)
        self.product.save()

        self.price = Price(store=self.store, price=100, product=self.product)
        self.price.save()

        self.store_detail = StoreViewSet.as_view({'get': 'retrieve'})
        self.store_list = StoreViewSet.as_view({'get': 'list'})
        self.store_products = StoreViewSet.as_view({'get': 'products'})

        self.url = '/stores/'

    def test_list(self) -> None:
        request = self.factory.get(path=self.url)
        response = self.store_list(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

        results = response.data['results'][0]

        self.assertEqual(results['name'], self.store.name)
        self.assertEqual(results['slug'], self.store.slug)
        self.assertEqual(results['url'], self.store.url)

        store_products = reverse_lazy(
            'store-products', kwargs={'slug': self.store.slug})

        self.assertEqual(results['products'], store_products)

    def test_retrieve(self) -> None:
        request = self.factory.get(path=self.url)
        response = self.store_detail(request, slug=self.store.slug)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.store.name)
        self.assertEqual(response.data['slug'], self.store.slug)
        self.assertEqual(response.data['url'], self.store.url)

        store_prices = reverse_lazy(
            'store-products', kwargs={'slug': self.store.slug})

        self.assertEqual(response.data['products'], store_prices)

    def test_list_store_products(self) -> None:
        request = self.factory.get(path=self.url)
        response = self.store_products(request, slug=self.store.slug)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

        results = response.data['results'][0]

        self.assertEqual(results['name'], self.product.name)
        self.assertEqual(results['price'], self.price.price)
