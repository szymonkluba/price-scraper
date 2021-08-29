from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    popularity = models.PositiveIntegerField(default=0)

    category = models.ForeignKey("Category", related_name="products", on_delete=models.RESTRICT)

    def __str__(self):
        return self.name
