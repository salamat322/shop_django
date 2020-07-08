from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware

from decimal import Decimal

from .cart import Cart
from .forms import AddToCartForm
from apps.products.models import Product


class CartTests(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('/')
        middleware = SessionMiddleware()
        middleware.process_request(self.request)
        self.request.session.save()

        self.product = Product(
            id=1,
            name='hat',
            price=Decimal('15.00'),
            in_stock=5,
        )

        self.product2 = Product(
            id=2,
            name='cap',
            price=Decimal('123.00'),
            in_stock=10
        )

    def test_cart_form(self):
        """test for AddToCartForm"""
        form_data = {'quantity': 10, 'update': True}
        form = AddToCartForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_init_cart(self):
        """test for create cart session"""
        request = self.request
        cart = Cart(request)
        self.assertEqual(cart.cart, {})

    def test_cart_add(self):
        """test for add product qty"""
        cart = Cart(self.request)
        cart.add(product=self.product,
                 quantity=4,
                 update_quantity=False)
        new_cart = {
            '1': {
                'price': '15.00',
                'quantity': 4,
            },
        }
        self.assertEqual(cart.cart, new_cart)

    def test_cart_add_update(self):
        """test for update product qty"""
        cart = Cart(self.request)
        cart.add(product=self.product,
                 quantity=10,
                 update_quantity=True,
                 )
        new_cart = {
            '1': {
                'quantity': 10,
                'price': '15.00',
                },
        }
        self.assertEqual(cart.cart, new_cart)

    def test_add_new_product_cart(self):
        cart = Cart(self.request)
        cart.add(product=self.product2,
                 quantity=3,
                 update_quantity=False,)
        new_cart = {
            '2': {
                'quantity': 3,
                'price': '123.00'
            }
        }
        self.assertEqual(cart.cart, new_cart)

    def test_remove_product_cart(self):
        cart = Cart(self.request)
        cart.remove(product=self.product)
        self.assertEqual(cart.cart, {})



