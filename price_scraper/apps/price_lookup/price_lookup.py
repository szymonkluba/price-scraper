import re
import requests
from bs4 import BeautifulSoup
from requests import RequestException

from .models import StoreSelectors


class NoPageFoundException(Exception):
    def __init__(self, message):
        self.message = message


class NoConnectionException(Exception):
    def __init__(self, message):
        self.message = message


class LookupWebsite:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    def __init__(self, url):
        self.website = self.get_website(url)

    def get_website(self, url):
        try:
            website = requests.get(url, headers=self.headers)
        except RequestException as exception:
            print(exception)
            raise NoConnectionException('Problem z połączeniem')
        if website.status_code != 200:
            raise NoPageFoundException('Nie znaleziono strony produktu')
        return website

    def get_website_as_text(self):
        return self.website.text


class PriceLookup:

    def __init__(self, website: LookupWebsite, search_params: StoreSelectors):
        self.soup = BeautifulSoup(website.get_website_as_text(), 'lxml')
        self.price_class = search_params.price_class
        self.available_class = search_params.available_class
        self.image_class = search_params.image_class

    def get_price(self):
        price_tag = self.soup.select_one(self.price_class)
        if price_tag:
            if price_tag.get('content'):
                price = price_tag.get('content')
            elif price_tag.string:
                price = price_tag.string
            else:
                price = str(price_tag)
            price = re.findall(r'\d*\s*\d*\s*\d+', str(price))
            if price:
                return float(price[0].replace(' ', '').replace(u'\n', '').replace(u'\xa0', ''))
        return

    def get_availability(self):
        availability_tag = self.soup.select_one(self.available_class)
        if availability_tag:
            is_buyable = availability_tag.get('is-buyable')
            if is_buyable is not None and not is_buyable:
                return True
            return False
        return True

    def get_image_url(self):
        image_tag = self.soup.select_one(self.image_class)
        if image_tag:
            url = image_tag.get('data-src')
            if url:
                if 'http' in url:
                    return url
