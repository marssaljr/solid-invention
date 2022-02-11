from django.test import TestCase, Client
from django.urls import reverse
from projects.models import Project


class TestProjectViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.projects = reverse('projects')
        self.project = reverse(
            "project",
            args=[
                1,
            ],
        )
        self.project1 = Project.objects.create(
            title="Project1", description="description", body="body"
        )

    def test_returns_projects_list_page(self):
        response = self.client.get(self.projects)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects.html')
