from django.db import models

# Create your models here.

class Book(models.Model):
  name = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  def __str__(self):
    return self.name

class Article(models.Model):
    title = models.CharField(max_length=40)
    time = models.DateField()
    description = models.CharField(max_length=400)
    body = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.title