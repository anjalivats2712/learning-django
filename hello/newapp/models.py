from django.db import models

# Create your models here. okk let me create it

class contact(models.Model):
    email=models.CharField(max_length=122)
    query=models.TextField(max_length=1000)
    notify=models.BooleanField()
    