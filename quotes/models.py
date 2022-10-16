from django.db import models

# Create your models here.
class Quote(models.Model):
    body = models.CharField(max_length=400)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
