from django.db import models


# Create your models here. okk let me create it

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    query=models.TextField(max_length=1000)
    date=models.DateField()
    #notify=models.BooleanField(default=True)
    #date=models.DateField()
   