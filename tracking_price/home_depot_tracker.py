from bs4 import BeautifulSoup

from .price_tracker import Tracker


class HomeDepotTracker(Tracker):

    _selector = "ciItemPrice"

    def filter_price(self, html):
        soup = BeautifulSoup(html, "html.parser")
        dom = soup.find(id=self._selector)
        return dom['value']
