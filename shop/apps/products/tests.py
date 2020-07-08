from django.test import TestCase
from django.urls import reverse

from .models import Product
from apps.categories.models import Category


class TestProduct(TestCase):

    def setUp(self):
        self.category = Category(name='pants', slug='pants')
        self.product = Product(name='pant', slug='pant', price=1000.00, in_stock=True, category=self.category)

    def test_product_list(self):
        response = self.client.get(reverse('products-list'))
        self.assertEqual(response.status_code, 200)

    def test_product_list_slug(self):
        self.assertEqual(self.category.get_absolute_url(), reverse('product-category', args=[self.category.slug]))
