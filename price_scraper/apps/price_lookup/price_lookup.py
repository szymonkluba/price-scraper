import re

import requests
from bs4 import BeautifulSoup

from .models import StoreSearchDetails


class NoPageFoundException(Exception):
    pass


class LookupWebsite:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    def __init__(self, url):
        self.website = self.get_website(url)

    def get_website(self, url):
        website = requests.get(url, headers=self.headers)
        if website.status_code != 200:
            raise NoPageFoundException("No page found for given URL")
        return website

    def get_website_as_text(self):
        return self.website.text


class PriceLookup:

    def __init__(self, website: LookupWebsite, search_params: StoreSearchDetails):
        self.soup = BeautifulSoup(website, "lxml")
        self.price_class = search_params.price_class
        self.available_class = search_params.available_class

    def get_price(self):
        price_tag = self.soup.select_one(self.price_class)
        if price_tag.get("content"):
            return float(price_tag.get("content"))
        price = re.findall(r"\d*\s*\d*\s*\d+", price_tag.string)
        if price:
            return float(price[0].replace(" ", ""))
        return

    def get_availability(self):
        availability_tag = self.soup.select_one(self.available_class)
        if availability_tag:
            return False
        return True
