from django.db import models


class StoreSearchDetails(models.Model):
    title_class = models.CharField(max_length=50)
    price_class = models.CharField(max_length=50)
    available_class = models.CharField(max_length=50)

    store = models.OneToOneField("stores.Store", related_name="search_details", on_delete=models.CASCADE, unique=True)


class ProductSearchDetails(models.Model):

    class Meta:
        unique_together = ["store", "product"]

    search_url = models.URLField()

    product = models.ForeignKey("products.Product", related_name="links", on_delete=models.CASCADE)
    store = models.ForeignKey("stores.Store", related_name="products_links", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store.name}: {self.product.name}"


class Price(models.Model):
    price = models.FloatField()
    available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey("products.Product", related_name="product_prices", on_delete=models.CASCADE)
    store = models.ForeignKey("stores.Store", related_name="store_prices", on_delete=models.CASCADE)

