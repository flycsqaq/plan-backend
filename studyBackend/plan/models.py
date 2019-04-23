from django.db import models

# Create your models here.
class Plan(models.Model):
  title = models.CharField(max_length=40)
  time = models.DateField()
  isCompleted = models.BooleanField(default=False)
  description = models.CharField(max_length=400)
  def __str__(self):
    return self.title