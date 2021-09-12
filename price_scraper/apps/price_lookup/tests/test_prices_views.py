from apps.price_lookup.models import Price
from apps.price_lookup.views import PricesViewSet
from apps.products.models import Category
from apps.products.models import Product
from apps.stores.models import Store
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase


class PricesViewsTests(APITestCase):
    PRODUCT1_PRICE = 100
    PRODUCT2_PRICE = 9001

    def setUp(self) -> None:
        self.factory = APIRequestFactory()

        category = Category.objects.create(name='TestCategory')

        self.product1 = Product(name='TestProduct1', category=category)
        self.product1.save()

        self.product2 = Product(name='TestProduct2', category=category)
        self.product2.save()

        self.store = Store(name='TestStore', url='https://test.com')
        self.store.save()

        Price.objects.create(price=self.PRODUCT1_PRICE,
                             product=self.product1, store=self.store)
        Price.objects.create(price=self.PRODUCT2_PRICE,
                             product=self.product2, store=self.store)

        self.prices = PricesViewSet.as_view({'get': 'list'})

        self.url = '/prices/'

    def test_list_prices(self) -> None:
        request = self.factory.get(self.url)
        response = self.prices(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

        results = response.data['results']

        self.assertEqual(results[0]['price'], self.PRODUCT1_PRICE)
        self.assertEqual(results[0]['store'], self.store.name)
        self.assertTrue(results[0]['available'])

        self.assertEqual(results[1]['price'], self.PRODUCT2_PRICE)
        self.assertEqual(results[1]['store'], self.store.name)
        self.assertTrue(results[1]['available'])

    def test_filter_prices(self) -> None:
        request = self.factory.get(self.url, {'product': self.product1.slug})
        response = self.prices(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

        result = response.data['results'][0]

        self.assertEqual(result['price'], self.PRODUCT1_PRICE)
