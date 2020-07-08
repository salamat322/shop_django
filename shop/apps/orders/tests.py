from django.test import TestCase
from django.urls import reverse
from decimal import Decimal

from .models import Order, OrderItem
from .forms import OrderCreateForm

from apps.products.models import Product


class OrderTest(TestCase):

    def setUp(self):
        self.order = Order(first_name='name', last_name='surname', email='some@gmail.com',
                           address='some address', city='some city', paid=False)
        self.product = Product(
            id=1,
            name='hat',
            price=Decimal('15.00'),
            in_stock=5,
        )
        self.order_item = OrderItem(quantity=1, price='100', product=self.product, order=self.order)

    def test_order_create_form(self):
        """test for OrderCreateForm"""
        form_data = {'first_name': 'name',
                     'last_name': 'surname',
                     'email': 'some@gmail.com',
                     'address': 'some address',
                     'city': 'some city'}
        form = OrderCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_get_cost(self):
        """test for get order cost"""
        cost = self.order_item.price * self.order_item.quantity
        self.assertEqual(self.order_item.get_cost(), cost)

    def test_get_total_cost(self):
        """test for model method"""
        total_cost = sum(self.order_item.get_cost() for self.order_item in self.order.items.all())
        self.assertEqual(self.order.get_total_cost(), total_cost)

    def get_create_order(self):
        response = self.client.get(reverse('create-order'))
        self.assertEqual(response.status_code, 200)