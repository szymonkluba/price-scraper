from django.db import models


class StoreSearchDetails(models.Model):
    class Meta:
        verbose_name_plural = 'Stores Search Details'

    title_class = models.CharField(max_length=50)
    price_class = models.CharField(max_length=50)
    available_class = models.CharField(max_length=50)

    store = models.OneToOneField(
        'stores.Store', related_name='search_details', on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f'Selectors: {self.store.name}'


class ProductSearchDetails(models.Model):
    class Meta:
        unique_together = ['store', 'product']
        verbose_name_plural = 'Product Search Details'

    search_url = models.URLField()

    product = models.ForeignKey(
        'products.Product', related_name='links', on_delete=models.CASCADE)
    store = models.ForeignKey(
        'stores.Store', related_name='products_links', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.store.name}: {self.product.name}'


class Price(models.Model):
    price = models.FloatField()
    available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(
        'products.Product', related_name='product_prices', on_delete=models.CASCADE)
    store = models.ForeignKey(
        'stores.Store', related_name='store_prices', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.store.name} - {self.timestamp}: ' \
               f"{self.product.name[:25] + '...' if len(self.product.name) > 25 else self.product.name} - {self.price}"
