from django.test import TestCase

from .models import Category


class CategoryTest(TestCase):

    def test_create_category(self):
        NAME = "Karty graficzne"

        category = Category.objects.create(name=NAME)
        self.assertEqual(category.name, NAME)

    def test_create_store(self):
