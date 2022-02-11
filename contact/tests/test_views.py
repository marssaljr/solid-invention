from django.test import (
    TestCase,
    Client,
    AsyncClient,
    modify_settings,
    override_settings,
)
from django.test.client import RequestFactory
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from contact.views import contactView
from icecream import ic
from config import settings


class TestViews(TestCase):
    def setUp(self):
        self.rf = RequestFactory()
        self.asclient = AsyncClient(SERVER_NAME="localhost")
        self.client = Client(SERVER_NAME="localhost")
        self.contact = reverse("contact")

    def test_contact_page_returns(self):
        response = self.client.get(self.contact)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "email.html")

    def test_contact_page_sendmail_success(self):
        request = self.rf.post(
            self.contact,
            {"name": "andre", "email": "andre@gmail.com", "message": "email test case"},
        )
        response = contactView(request)
        assert response.status_code == 200

    def test_contact_page_form_is_invalid(self):
        response = self.client.post(
            self.contact, {"name": "", "email": "", "message": ""}
        )
        self.assertEqual(response.status_code, 400)
        assert len(response.context["error"]) >= 2
        self.assertTemplateUsed(response, "email.html")
