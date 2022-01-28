from django.db import models
import readtime
from django.urls import reverse
from tinymce import models as tinymce_models

class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
      return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    content = tinymce_models.HTMLField('Content')

    def get_readtime(self):
      result = readtime.of_text(self.content)
      return result.text 

    def __str__(self):
      return self.title

    def get_absolute_url(self):
      return reverse('post-detail', kwargs={
        'id': self.id,
        'title': self.title,
      })