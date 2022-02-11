from django.urls import reverse, resolve
from django.test import TestCase, Client


class PortfolioTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.home = reverse("home")

    def test_home_page_resolves(self):
        response = self.client.get(self.home)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
