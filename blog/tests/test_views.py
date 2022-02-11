from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.posts = reverse("blog_list")
        self.post = reverse(
            "post",
            args=[
                1,
            ],
        )
        self.post1 = Post.objects.create(
            title="post1", description="description", body="body"
        )

    def test_returns_blog_list_page(self):
        response = self.client.get(self.posts)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")

    def test_returns_post_page(self):
        response = self.client.get(self.post)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post.html")
