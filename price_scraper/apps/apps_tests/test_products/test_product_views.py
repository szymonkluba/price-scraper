from apps.price_lookup.models import StoreSelectors
from apps.products.models import Category
from apps.products.models import Product
from apps.products.views import ProductViewSet
from apps.stores.models import Store
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from unittest.mock import patch


# noinspection DuplicatedCode
class ProductViewsTest(APITestCase):
    EMPTY_PAGE = '<html></html>'
    PAGE_ONE_STORE_DETAILS = '<html><head></head><body><p class="price">100</p></body></html>'
    PAGE_WITH_IMAGE = '<html><head></head><body><img class="image" data-src="http://test_url/"><p class="price">100</p></body></html>'

    def setUp(self) -> None:
        self.factory = APIRequestFactory()

        self.category = Category(name='TestCategory')
        self.category.save()

        self.product = Product(name='TestProduct', category=self.category)
        self.product.save()

        self.product_detail = ProductViewSet.as_view({'get': 'retrieve'})
        self.product_list = ProductViewSet.as_view({'get': 'list'})
        self.update_prices = ProductViewSet.as_view({'get': 'update_prices'})

        self.url = '/products/'

    def test_list(self) -> None:
        request = self.factory.get(self.url)
        response = self.product_list(request)

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
            'in_favs': False
        })

    def test_retrieve(self) -> None:
        request = self.factory.get(self.url)
        response = self.product_detail(request, slug=self.product.slug)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'name': self.product.name,
            'slug': self.product.slug,
            'url': reverse_lazy('product-detail', kwargs={'slug': self.product.slug}),
            'popularity': 0,
            'category': self.category.name,
            'category_link': reverse_lazy('category-detail', kwargs={'slug': self.category.slug}),
            'current_prices': [],
            'image_url': None,
            'in_favs': False
        })

    def test_popularity_counter(self) -> None:
        request = self.factory.get(self.url)
        response = self.product_detail(request, slug=self.product.slug)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['popularity'], 0)

        response = self.product_detail(request, slug=self.product.slug)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['popularity'], 1)

    def test_update_prices_no_product_page_found(self) -> None:
        store1 = Store.objects.create(name='TestStore1', url='')

        self.product.links.create(search_url='https://test.html', store=store1)

        with patch('requests.get') as mock:
            mock.status_code = status.HTTP_404_NOT_FOUND

            request = self.factory.get(self.url)
            response = self.update_prices(
                request=request, slug=self.product.slug)

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(response.data, {
                'errors': ['TestStore1: Nie znaleziono strony produktu']
            })

    def test_could_not_update_price_all_stores(self) -> None:
        store1 = Store.objects.create(name='TestStore1', url='')
        StoreSelectors.objects.create(
            store=store1,
            image_class='a',
            price_class='a',
            available_class='a'
        )

        self.product.links.create(search_url='https://test.html', store=store1)

        with patch('apps.price_lookup.price_lookup.LookupWebsite') as MockClass:
            instance = MockClass()
            instance.get_website_as_text.return_value = self.EMPTY_PAGE

            request = self.factory.get(self.url)
            response = self.update_prices(
                request=request, slug=self.product.slug)

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_could_not_update_price_some_stores(self) -> None:
        store1 = Store.objects.create(name='TestStore1', url='')
        StoreSelectors.objects.create(
            store=store1,
            image_class='.title',
            price_class='.price',
            available_class='.av'
        )

        store2 = Store.objects.create(name='TestStore2', url='')
        StoreSelectors.objects.create(
            store=store2,
            image_class='.a',
            price_class='.a',
            available_class='.a'
        )

        self.product.links.create(search_url='https://test.html', store=store1)
        self.product.links.create(search_url='https://test.html', store=store2)

        with patch('apps.price_lookup.price_lookup.LookupWebsite') as MockClass:
            instance = MockClass()
            instance.get_website_as_text.return_value = self.PAGE_ONE_STORE_DETAILS

            request = self.factory.get(self.url)
            response = self.update_prices(
                request=request, slug=self.product.slug)

            self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
            self.assertEqual(response.data, {
                'errors': ['Nie udało się zaktualizować ceny dla sklepu: TestStore2']
            })

    def test_update_prices(self) -> None:
        store1 = Store.objects.create(name='TestStore1', url='')
        StoreSelectors.objects.create(
            store=store1,
            image_class='.title',
            price_class='.price',
            available_class='.av'
        )

        store2 = Store.objects.create(name='TestStore2', url='')
        StoreSelectors.objects.create(
            store=store2,
            image_class='.title',
            price_class='.price',
            available_class='.av'
        )

        self.product.links.create(search_url='https://test.html', store=store1)
        self.product.links.create(search_url='https://test.html', store=store2)

        with patch('apps.price_lookup.price_lookup.LookupWebsite') as MockClass:
            instance = MockClass()
            instance.get_website_as_text.return_value = self.PAGE_ONE_STORE_DETAILS

            self.assertEqual(len(self.product.product_prices.all()), 0)

            request = self.factory.get(self.url)
            response = self.update_prices(
                request=request, slug=self.product.slug
            )

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(self.product.product_prices.all()), 2)
            self.assertEqual(response.data, {'errors': []})

    def test_updates_product_image(self) -> None:
        store1 = Store.objects.create(name='TestStore1', url='')
        StoreSelectors.objects.create(
            store=store1,
            image_class='.image',
            price_class='.price',
            available_class='.av'
        )

        self.product.links.create(
            search_url='https://test.html/', store=store1)

        with patch('apps.price_lookup.price_lookup.LookupWebsite') as MockClass:
            instance = MockClass()
            instance.get_website_as_text.return_value = self.PAGE_WITH_IMAGE

            request = self.factory.get(self.url)
            response = self.update_prices(
                request=request, slug=self.product.slug
            )

            updated_product = Product.objects.get(slug=self.product.slug)

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(updated_product.image_url, 'http://test_url/')

    def test_does_not_change_url_if_present(self):
        store1 = Store.objects.create(name='TestStore1', url='')
        StoreSelectors.objects.create(
            store=store1,
            image_class='.image',
            price_class='.price',
            available_class='.av'
        )

        self.product.links.create(
            search_url='https://test.html/', store=store1)

        self.product.image_url = 'different_url'
        self.product.save()

        with patch('apps.price_lookup.price_lookup.LookupWebsite') as MockClass:
            instance = MockClass()
            instance.get_website_as_text.return_value = self.PAGE_WITH_IMAGE

            request = self.factory.get(self.url)
            response = self.update_prices(
                request=request, slug=self.product.slug
            )

            updated_product = Product.objects.get(slug=self.product.slug)

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(updated_product.image_url, 'different_url')
