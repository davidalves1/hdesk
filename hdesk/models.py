from django.db import models
from django.utils import timezone

# Create your models here.

'''
Model to Task
'''
class Task(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    mail = models.CharField(max_length=150)
    description = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def save_task(self):
        self.updated_at = timezone.now()
        self.save()
