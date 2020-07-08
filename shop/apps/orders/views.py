from django.shortcuts import render, redirect
from django.urls import reverse

from .models import OrderItem
from .forms import OrderCreateForm

from apps.carts.cart import Cart


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for product in cart:
                OrderItem.objects.create(order=order,
                                         product=product['product'],
                                         price=product['price'],
                                         quantity=product['quantity'])
            cart.clear()
            request.session['order_id'] = order.id
            return redirect(reverse('process'))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order_form.html', locals())