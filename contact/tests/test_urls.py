from contact.views import contactView
from django.urls import reverse, resolve
from django.test import TestCase

class ContactTestCase(TestCase):
    def test_contact_page_resolves(self):
        response = reverse('contact')
        self.assertEqual(resolve(response).func.__name__, contactView.__name__)
