from django.test import TestCase
# my imports

from django.contrib.auth import get_user_model
from django.urls import reverse
from blog.models import Post

# Create your tests here.


class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@mail.com',
            password='secret'
        )
        self.post = Post.objects.create(
            title='A very good title',
            body='Some interesting stuff',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A sample test')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A very good title')
        self.assertEqual(f'{self.post.body}', 'Some interesting stuff')
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_post_list_view(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Some interesting stuff')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A very good title')
        self.assertContains(response, 'Some interesting stuff')  # to check that the content of body is also present
        self.assertTemplateUsed(response, 'post_detail.html')
