from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from apps.products.models import Product

from .cart import Cart
from .forms import AddToCartForm


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'], update_quantity=cd['update'])

    return redirect('cart-detail')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart-detail')


def cart_detail(request):
    cart = Cart(request)
    for product in cart:
        product['update_quantity_form'] = AddToCartForm(initial={'quantity': product['quantity'], 'update': True})
    return render(request, 'carts/cart_detail.html', locals())


def cart(request):
    return {'cart': Cart(request)}