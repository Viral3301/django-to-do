from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    task_title = models.CharField(max_length=30)
    task_body = models.TextField(blank=True)
    deadline = models.DateField(blank=True,null=True)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_title
    
    def get_absolute_url(self):
        return reverse('home')