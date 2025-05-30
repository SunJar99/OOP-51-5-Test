from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post, Comment
from django.contrib.auth.models import User

class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(author=self.user, title='Test Post', body='This is a test post.', is_published=True)

    def test_create_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('post-list'), {'title': 'New Post', 'body': 'New post body.', 'is_published': True})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_post_list(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_post_detail(self):
        response = self.client.get(reverse('post-detail', args=[self.post.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)

    def test_update_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.put(reverse('post-detail', args=[self.post.id]), {'title': 'Updated Title', 'body': 'Updated body.', 'is_published': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')

    def test_delete_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(reverse('post-detail', args=[self.post.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

class CommentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(author=self.user, title='Test Post', body='This is a test post.', is_published=True)
        self.comment = Comment.objects.create(post=self.post, author=self.user, body='This is a test comment.', is_approved=True)

    def test_add_comment(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('post-comments', args=[self.post.id]), {'body': 'New comment.'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_comments(self):
        response = self.client.get(reverse('post-comments', args=[self.post.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)