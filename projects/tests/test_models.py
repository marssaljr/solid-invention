from django.test import TestCase
from projects.models import *


class TestModels(TestCase):
    def setUp(self):
        self.project1 = Project.objects.create(
            title="title",
            description="Description",
            img="url",
            body="text",
        )
        self.python = Tag.objects.create(
            name="Python",
        )
        self.project2 = Project.objects.create(
            title="title2",
            description="Description",
            img="url",
            body="text",
        )

    def test_create_project(self):
        self.assertEqual(self.project1.title, "title")
        self.assertEqual(self.project1.body, "text")
        self.assertEqual(self.project1.img, "url")
        self.assertEqual(self.project1.description, "Description")
        self.assertEqual(str(self.project1), self.project1.title)

    def test_create_tag(self):
        self.assertEqual(self.python.name, "Python")
        self.assertEqual(str(self.python), self.python.name)

    def test_project_has_tag(self):
        self.project1.tags.add(self.python)
        self.assertEqual(self.project1.title, self.python.tags.values()[0].get("title"))

    def test_project_has_no_tag(self):
        self.assertFalse(len(self.project2.tags.values()) > 0)

    def test_delete_project(self):
        Project.delete(self.project1)
        self.assertFalse(self.project1.id)

    def test_delete_tag(self):
        Tag.delete(self.python)
        self.assertFalse(self.python.id)
