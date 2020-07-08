from django.db import models
from django.urls import reverse

from apps.categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.id, self.slug])
