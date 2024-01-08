from django.db import models
from django.utils import timezone

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=50)
    remark = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

