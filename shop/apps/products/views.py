from django.shortcuts import render, get_object_or_404

from .models import Product

from apps.categories.models import Category
from apps.carts.forms import AddToCartForm


def products_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(in_stock=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'products/products_list.html', locals())


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, in_stock=True)
    form = AddToCartForm()
    return render(request, 'products/product_detail.html', locals())
