from django.test import TestCase
from django.urls import reverse


class PaymentTest(TestCase):

    def test_done_payment(self):
        """test for success payment"""
        response = self.client.get(reverse('done'))
        self.assertEqual(response.status_code, 200)

    def test_cancelled(self):
        """test for canceled payment"""
        response = self.client.get(reverse('canceled'))
        self.assertEqual(response.status_code, 200)

    def test_payment_process(self):
        """test for payment process"""
        response = self.client.get(reverse('done'))
        self.assertEqual(response.status_code, 200)

