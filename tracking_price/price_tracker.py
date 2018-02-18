from bs4 import BeautifulSoup

import requests


class Tracker:

    def __init__(self, url):
        self._url = url
        self._html = self.fetch_html()
        self._price = self.filter_price(self._html)

    def fetch_html(self):
        return requests.get(self._url).text

    def filter_price(self, html):
        return 0

    def get_html(self):
        return self._html

    def get_price(self):
        return self._price

    def get_url(self):
        return self._url
