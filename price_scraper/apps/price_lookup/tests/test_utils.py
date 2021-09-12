import requests
from apps.price_lookup.price_lookup import LookupWebsite
from apps.price_lookup.price_lookup import NoConnectionException
from apps.price_lookup.price_lookup import NoPageFoundException
from apps.price_lookup.price_lookup import PriceLookup
from django.test import TestCase
from requests import exceptions
from rest_framework import status
from unittest.mock import MagicMock
from unittest.mock import patch


class LookupWebsiteTests(TestCase):
    TEST_PAGE = '<html><head></head><body></body></html>'

    def test_raise_no_page_found_exception(self) -> None:
        with patch('requests.get') as mock:
            instance = mock(status_code=status.HTTP_404_NOT_FOUND)

            with self.assertRaises(NoPageFoundException):
                LookupWebsite('test.html')

    def test_returns_page_as_text(self) -> None:
        with patch('requests.get') as mock:
            instance = mock()
            instance.status_code = status.HTTP_200_OK
            instance.text = self.TEST_PAGE

            website = LookupWebsite('test.html')

            self.assertEqual(website.get_website_as_text(), self.TEST_PAGE)

    def test_raises_no_connection_exception(self) -> None:
        with patch.object(requests, 'get', side_effect=exceptions.ConnectionError()):
            with self.assertRaises(NoConnectionException):
                LookupWebsite('http://test.com')

        with patch.object(requests, 'get', side_effect=exceptions.Timeout()):
            with self.assertRaises(NoConnectionException):
                LookupWebsite('http://test.com')

        with patch.object(requests, 'get', side_effect=exceptions.TooManyRedirects()):
            with self.assertRaises(NoConnectionException):
                LookupWebsite('http://test.com')

        with patch.object(requests, 'get', side_effect=exceptions.HTTPError()):
            with self.assertRaises(NoConnectionException):
                LookupWebsite('http://test.com')


class PriceLookupSelectorsTests(TestCase):
    PAGE_PRICE_WITH_CLASS = '<html><head></head><body><p class="price">100</p></body></html>'
    PAGE_PRICE_WITH_ID = '<html><head></head><body><p id="price">100</p></body></html>'
    PAGE_PRICE_IN_CONTENT = '<html><head></head><body><p id="price" content="100.00"></p></body></html>'
    PAGE_WITH_IMAGE = '<html><head></head><body><img class="image" data-src="http://test_url/"></p></body></html>'

    def setUp(self) -> None:
        self.website = MagicMock()
        self.search_params = MagicMock()

    def test_finds_value_by_class(self):
        self.website.get_website_as_text = MagicMock(
            return_value=self.PAGE_PRICE_WITH_CLASS)
        self.search_params.price_class = '.price'

        price_lookup = PriceLookup(self.website, self.search_params)

        self.assertEqual(price_lookup.get_price(), 100)

    def test_finds_value_by_id(self):
        self.website.get_website_as_text = MagicMock(
            return_value=self.PAGE_PRICE_WITH_ID)
        self.search_params.price_class = '#price'

        price_lookup = PriceLookup(self.website, self.search_params)

        self.assertEqual(price_lookup.get_price(), 100)

    def test_finds_value_by_selectors_path(self):
        self.website.get_website_as_text = MagicMock(
            return_value=self.PAGE_PRICE_WITH_ID)
        self.search_params.price_class = 'html > body > p'

        price_lookup = PriceLookup(self.website, self.search_params)

        self.assertEqual(price_lookup.get_price(), 100)

    def test_get_value_from_content(self):
        self.website.get_website_as_text = MagicMock(
            return_value=self.PAGE_PRICE_WITH_ID)
        self.search_params.price_class = '#price'

        price_lookup = PriceLookup(self.website, self.search_params)

        self.assertEqual(price_lookup.get_price(), 100)

    def test_get_image_url_from_src(self):
        self.website.get_website_as_text = MagicMock(
            return_value=self.PAGE_WITH_IMAGE)
        self.search_params.image_class = '.image'

        price_lookup = PriceLookup(self.website, self.search_params)

        self.assertEqual(price_lookup.get_image_url(), 'http://test_url/')


class PriceLookupValuesTests(TestCase):
    PAGE_NO_NUMBERS = '<html><head></head><body><p id="price">abc</p></body></html>'
    PAGE_NO_NUMBERS_IN_CONTENT = '<html><head></head><body><p id="price" content="abc"></p></body></html>'
    PAGE_PRICE_WITH_CURRENCY = '<html><head></head><body><p id="price">100.00zł</p></body></html>'

    def setUp(self) -> None:
        self.website = MagicMock()
        self.search_params = MagicMock()

    def test_non_numeric_values(self):
        self.website.get_website_as_text = MagicMock(
            return_value=self.PAGE_NO_NUMBERS)
        self.search_params.price_class = '#price'

        price_lookup = PriceLookup(self.website, self.search_params)

        self.assertIsNone(price_lookup.get_price())

    def test_non_numeric_values_in_content(self):
        self.website.get_website_as_text = MagicMock(
            return_value=self.PAGE_NO_NUMBERS_IN_CONTENT)
        self.search_params.price_class = '#price'

        price_lookup = PriceLookup(self.website, self.search_params)

        self.assertIsNone(price_lookup.get_price())

    def test_values_with_currency(self):
        self.website.get_website_as_text = MagicMock(
            return_value=self.PAGE_PRICE_WITH_CURRENCY)
        self.search_params.price_class = '#price'

        price_lookup = PriceLookup(self.website, self.search_params)

        self.assertEqual(price_lookup.get_price(), 100)


class PriceLookupItemAvailabilityTests(TestCase):
    PAGE_ITEM_OUT_OF_STOCK = '<html><head></head><body><p class="av">Ni ma:(</p></body></html>'
    PAGE_ITEM_IS_BUYABLE_PROP = '<html><head></head><body><av is-buyable="0">Ni ma:(</av></body></html>'
    PAGE_PRICE_WITH_CLASS = '<html><head></head><body><p class="price">100</p></body></html>'

    def setUp(self) -> None:
        self.website = MagicMock()
        self.search_params = MagicMock()
        self.search_params.available_class = '.av'

    def test_item_unavailable(self):
        self.website.get_website_as_text = MagicMock(
            return_value=self.PAGE_ITEM_OUT_OF_STOCK)

        price_lookup = PriceLookup(self.website, self.search_params)

        self.assertFalse(price_lookup.get_availability())

    def test_item_available(self):
        self.website.get_website_as_text = MagicMock(
            return_value=self.PAGE_PRICE_WITH_CLASS)

        price_lookup = PriceLookup(self.website, self.search_params)

        self.assertTrue(price_lookup.get_availability())

    def test_item_with_is_buayble_prop(self):
        self.search_params.available_class = 'av'
        self.website.get_website_as_text = MagicMock(
            return_value=self.PAGE_ITEM_IS_BUYABLE_PROP)

        price_lookup = PriceLookup(self.website, self.search_params)

        self.assertFalse(price_lookup.get_availability())
