from django.test import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch

from ...price_lookup.models import Price
from ...products.utils import NoPriceUpdateException
from ...products.utils import update_product_prices


class ProductPricesUpdateTests(TestCase):

    def setUp(self) -> None:
        self.product = MagicMock()
        self.search_params = MagicMock()
        self.store = MagicMock()
        self.search_params.store = self.store

    def test_creates_new_price(self) -> None:
        with patch('apps.price_lookup.price_lookup.LookupWebsite'):
            with patch('apps.price_lookup.price_lookup.PriceLookup') as MockPriceLookup:
                with patch.object(Price.objects, 'create') as mocked_price:
                    instance = MockPriceLookup()
                    instance.get_price = MagicMock(return_value=100)
                    instance.get_availability = MagicMock(return_value=True)
                    update_product_prices(self.product, self.search_params)

                    mocked_price.assert_called_once_with(
                        price=100,
                        available=True,
                        store=self.store,
                        product=self.product
                    )

    def test_raises_no_update_exception_no_price(self) -> None:
        with patch('apps.price_lookup.price_lookup.LookupWebsite'):
            with patch('apps.price_lookup.price_lookup.PriceLookup') as MockPriceLookup:
                instance = MockPriceLookup()
                instance.get_price = MagicMock(return_value=None)
                instance.get_availability = MagicMock(return_value=True)

                with self.assertRaises(NoPriceUpdateException):
                    update_product_prices(self.product, self.search_params)

    def test_raises_no_update_exception_no_availability(self) -> None:
        with patch('apps.price_lookup.price_lookup.LookupWebsite'):
            with patch('apps.price_lookup.price_lookup.PriceLookup') as MockPriceLookup:
                instance = MockPriceLookup()
                instance.get_price = MagicMock(return_value=100)
                instance.get_availability = MagicMock(return_value=None)

                with self.assertRaises(NoPriceUpdateException):
                    update_product_prices(self.product, self.search_params)
