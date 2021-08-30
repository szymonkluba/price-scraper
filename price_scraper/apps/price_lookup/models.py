from django.db import models


class StoreSearchDetails(models.Model):
    title_class = models.CharField(max_length=50)
    price_class = models.CharField(max_length=50)
    available_class = models.CharField(max_length=50)

    store = models.ForeignKey("stores.Store", related_name="store_search", on_delete=models.CASCADE)


class ProductSearchDetails(models.Model):
    search_url = models.URLField()

    product = models.ForeignKey("products.Product", related_name="product_search", on_delete=models.CASCADE)
    store = models.ForeignKey("stores.Store", related_name="search_details", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store.name}: {self.product.name}"


class Price(models.Model):
    price = models.FloatField()
    available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey("products.Product", related_name="product_prices", on_delete=models.CASCADE)
    store = models.ForeignKey("stores.Store", related_name="store_prices", on_delete=models.CASCADE)

