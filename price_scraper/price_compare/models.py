from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class Price(models.Model):
    price = models.FloatField(null=False, blank=False)
    available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey("Product", related_name="product_prices", on_delete=models.CASCADE)
    store = models.ForeignKey("Store", related_name="store_prices", on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    slug = models.CharField(max_length=200, null=False, unique=True)
    popularity = models.PositiveIntegerField()

    category = models.ForeignKey("Category", related_name="products", on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class SearchDetails(models.Model):
    search_url = models.URLField()
    product_card = models.CharField(max_length=50)
    title_class = models.CharField(max_length=50)
    price_class = models.CharField(max_length=50)
    available_class = models.CharField(max_length=50)

    product = models.ForeignKey("Product", related_name="product_details", on_delete=models.CASCADE)
    store = models.ForeignKey("Store", related_name="search_details", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store.name}: {self.product.name}"


class Store(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.name
