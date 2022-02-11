from django.test import TestCase
from django.urls import resolve, reverse
from projects.views import ProjectsListView, ProjectView


class ProjectsTestCase(TestCase):
    def test_projects_page_resolves(self):
        view = reverse("projects")
        self.assertEqual(
            resolve(view).func.__name__, ProjectsListView.as_view().__name__
        )

    def test_single_project_page_resolves(self):
        view = reverse(
            "project",
            args=[
                1,
            ],
        )
        self.assertEqual(resolve(view).func.__name__, ProjectView.as_view().__name__)
