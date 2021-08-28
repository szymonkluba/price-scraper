from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Price(models.Model):
    price = models.FloatField()
    available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey("Product", related_name="product_prices", on_delete=models.CASCADE)
    store = models.ForeignKey("stores.Store", related_name="store_prices", on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    popularity = models.PositiveIntegerField(default=0)

    category = models.ForeignKey("Category", related_name="products", on_delete=models.RESTRICT)

    def __str__(self):
        return self.name
