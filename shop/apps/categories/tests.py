from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Category


class TestCategory(TestCase):
    urls = 'apps.categories.urls'

    def setUp(self):
        self.category = Category(name='pants', slug='pants')
        self.client = Client()
        user = User.objects.create_superuser(
            username='test',
            password='test',
        )
        self.client.force_login(user)

    def test_get_absolute_url(self):
        """test for get absolute url"""
        self.assertEqual(self.category.get_absolute_url(), reverse('product-category', args=[self.category.slug]))

    def test_admin_pages(self):
        self.client.login()
        admin_pages = [
            "/admin/",
            "/admin/auth/",
            "/admin/auth/group/",
            "/admin/auth/group/add/",
            "/admin/auth/user/",
            "/admin/auth/user/add/",
            "/admin/password_change/"

        ]
        for page in admin_pages:
            response = self.client.get(page)
            assert response.status_code == 200


