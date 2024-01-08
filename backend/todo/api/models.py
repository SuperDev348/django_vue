from django.db import models
from django.utils import timezone

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=50)
    remark = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     """Returns a string represontation of a message"""
    #     date = timezone.localtime(self.created_date)
    #     return f"'{self.title}' created on {date.strftime('%A, %d %B, %Y at %X')}"
