from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
# Create your tests here.


class TaskTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret'
        )

        self.post = Post.objects.create(
            task_title = 'A good title',
            task_body = 'Nice body content',
        )
    
    def test_string_representation(self):
        post = Post(task_title = 'A sample title')
        self.assertEqual(str(post),post.task_title)

    def test_get_absolute_url(self):
        self.assertEquals(self.post.get_absolute_url(),'/')

    def test_task_content(self):
        self.assertEqual(f'{self.post.task_title}','A good title')
        self.assertEqual(f'{self.post.task_body}','Nice body content')

    def test_task_list_view(self):
        response = self.client.get(reverse('home'),follow=True)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'A good title')
        self.assertTemplateUsed(response,'home.html')
    
    def test_task_detail_view(self):
        response = self.client.get('/task/1/')
        no_response = self.client.get('/task/10000000' ,follow=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'A good title')
        self.assertTemplateUsed(response,'task_detail.html')

    def test_task_create_view(self):
        response = self.client.post(reverse('create'),{
            'task_title' : 'New title',
            'task_body' : 'New text',
        },follow=True)
        self.assertEqual(response.status_code,200)


    def test_task_update_view(self):
        response = self.client.post(reverse('edit',args='1'),{
            'task_title' : 'Updated title',
            'task_body' : 'Updated text',
        })
        self.assertEqual(response.status_code,302)

    def test_task_delete_view(self):
        response = self.client.get(reverse('delete',args='1'))
        self.assertEqual(response.status_code,200)