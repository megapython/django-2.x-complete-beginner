from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):

    # Initial setup for testing
    def setUp(self):
        self.post = Post.objects.create(
            title='Some blog title',
            body='Awesome blog content'
        )

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        # Test Status Code
        self.assertEqual(response.status_code, 200)
        # Test Template Used
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_post_detail(self):
        response = self.client.get('/post/1/')
        response_not_found = self.client.get('/post/100/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_not_found.status_code, 404)
        self.assertContains(response, 'Some blog title')
        self.assertTemplateUsed(response, 'blog/post_detail.html')
