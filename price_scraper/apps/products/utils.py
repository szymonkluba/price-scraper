from ..price_lookup import price_lookup
from ..price_lookup.models import Price
from ..price_lookup.models import ProductLinks
from ..products.models import Product


class NoPriceUpdateException(Exception):

    def __init__(self, message):
        self.message = message


def update_product_prices(product: Product, product_links: ProductLinks):
    url = product_links.search_url
    store = product_links.store

    website = price_lookup.LookupWebsite(url)

    prices_scraper = price_lookup.PriceLookup(website, store.search_details)

    price = prices_scraper.get_price()
    available = prices_scraper.get_availability()
    image_url = prices_scraper.get_image_url()

    if product.image_url is None and image_url is not None:
        product.image_url = image_url

    if price is not None and available is not None:
        Price.objects.create(price=price, available=available,
                             store=store, product=product)
        return
    raise NoPriceUpdateException(
        f'Nie udało się zaktualizować ceny dla sklepu: {store.name}')
