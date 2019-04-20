from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=20)
    author= models.CharField(max_length=20)

    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('booklist', args=[])
