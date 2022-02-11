from django.test import TestCase, SimpleTestCase
from django.urls import resolve, reverse
from blog.views import BlogListView, PostView

# Create your tests here.
class BlogTestCase(TestCase):
    def test_blog_page_resolves(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, BlogListView.as_view().__name__)

    def test_single_post_page_resolves(self):
        url = reverse(
            "post",
            args=[
                1,
            ],
        )
        # print(resolve(url))
        self.assertEqual(resolve(url).func.__name__, PostView.as_view().__name__)
