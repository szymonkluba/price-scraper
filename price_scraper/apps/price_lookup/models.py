from django.db import models


class SearchDetails(models.Model):
    search_url = models.URLField()
    product_card = models.CharField(max_length=50)
    title_class = models.CharField(max_length=50)
    price_class = models.CharField(max_length=50)
    available_class = models.CharField(max_length=50)

    product = models.ForeignKey("products.Product", related_name="product_details", on_delete=models.CASCADE)
    store = models.ForeignKey("stores.Store", related_name="search_details", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store.name}: {self.product.name}"
