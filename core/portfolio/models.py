from email.policy import default
from turtle import title
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=125)
    content = models.TextField()
    github_url = models.URLField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=125)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title





