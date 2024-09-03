from django.db import models

# Create your models here.
class Task(models.Model):
    Name = models.CharField(max_length=100)
    task = models.CharField(max_length=100)

def _str_(self):
    return self.Name