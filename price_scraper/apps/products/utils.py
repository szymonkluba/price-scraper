from ..price_lookup import price_lookup
from ..price_lookup.models import ProductSearchDetails, Price
from ..products.models import Product


class NoPriceUpdateException(Exception):

    def __init__(self, message):
        self.message = message


def update_product_prices(product: Product, product_links: ProductSearchDetails):
    url = product_links.search_url
    store = product_links.store

    try:
        website = price_lookup.LookupWebsite(url)
    except price_lookup.NoPageFoundException:
        return

    prices_scraper = price_lookup.PriceLookup(website.get_website_as_text(), store.search_details)

    price = prices_scraper.get_price()
    available = prices_scraper.get_availability()

    if price and available:
        Price.objects.create(price=price, available=available, store=store, product=product)
        return
    raise NoPriceUpdateException(f"Nie udało się zaktualizować ceny dla sklepu: {store.name}")
