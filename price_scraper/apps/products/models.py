from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    class Meta:
        ordering = ('slug',)

    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    popularity = models.PositiveIntegerField(default=0)
    image_url = models.URLField(blank=True, null=True)

    category = models.ForeignKey(
        'Category', related_name='products', on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
