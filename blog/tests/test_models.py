from django.test import TestCase
from blog.models import *

class TestModels(TestCase):

    def setUp(self):
        self.post1 = Post.objects.create(
            title='',
            description='Description',
            img='url',
            body='',
        )
        self.technology = Tag.objects.create(
            name='Technology',
        )
        self.post2 = Post.objects.create(
            title='Post2',
            description='Description',
            img='url',
            body='body'
        )

    def test_post_has_tag(self):
        """
        ensure post2 has one tag
        """
        self.post2.tags.add(self.technology)
        self.assertEqual(self.post2.title, self.technology.tags.values()[0].get('title'))

    def test_post_has_no_tag(self):
        """
        ensure post2 has no tags
        """
        self.assertFalse(len(self.post2.tags.values()) > 0)

    def test_post_has_no_title(self):
        self.assertFalse(len(self.post1.title) > 0)

    def test_post_has_title(self):
        self.post1.title = 'Post1'
        self.assertEqual(self.post1.title, 'Post1')

    def test_post_has_body(self):
        self.post1.body = 'body'
        self.assertTrue(len(self.post1.body) >= 4)

    def test_post_has_no_body(self):
        self.assertFalse(len(self.post1.body) > 0)
