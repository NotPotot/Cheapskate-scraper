#the common interface every marketplace source has to follow
class MarketplaceSource:
    name = "base"

    def search(self, query, max_price):
        raise NotImplementedError

class SampleSource(MarketplaceSource):
    #sample without any API yet
    name = "sample"
    
    DEALS = [
        {"title": "iPhone 12 64GB - Good Condition", "price": 220.0, "currency": "USD",
         "url": "https://example.com/1", "image": "https://placehold.co/300x200?text=iPhone+12", "source": "sample"},
        {"title": "Sony WH-1000XM4 Headphones", "price": 180.0, "currency": "USD",
         "url": "https://example.com/2", "image": "https://placehold.co/300x200?text=Sony+XM4", "source": "sample"},
        {"title": "Nintendo Switch OLED", "price": 280.0, "currency": "USD",
         "url": "https://example.com/3", "image": "https://placehold.co/300x200?text=Switch", "source": "sample"},
        {"title": "Dyson V8 Vacuum", "price": 150.0, "currency": "USD",
         "url": "https://example.com/4", "image": "https://placehold.co/300x200?text=Dyson+V8", "source": "sample"},
    ]

    def search(self, query, max_price):
        results = self.DEALS
        if query:
            q = query.lower()
            results = [d for d in results if q in d["title"].lower()]
        if max_price is not None:
            results = [d for d in results if d["price"] <= max_price]
        return results
