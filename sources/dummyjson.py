#using dummy json because it doesnt require an api key
import requests

from sources.base import MarketplaceSource

SEARCH_URL = "https://dummyjson.com/products/search"


class DummyJsonSource(MarketplaceSource):
    name = "dummyjson"

    def search(self, query, max_price):
        if not query:
            return []

        response = requests.get(SEARCH_URL, params={"q": query})
        response.raise_for_status()
        products = response.json().get("products", [])

        deals = []
        for product in products:
            price = float(product.get("price", 0))
            if max_price is not None and price > max_price:
                continue
            deals.append({
                "title": product.get("title", ""),
                "price": price,
                "currency": "USD",
                "url": "https://dummyjson.com/products/" + str(product.get("id", "")),
                "image": product.get("thumbnail", ""),
                "source": "dummyjson",
            })
        return deals