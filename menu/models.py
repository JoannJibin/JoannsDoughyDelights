from django.db import models

# Create your models here.
class menu (models.Model):

    Name=models.CharField(max_length=500)
    Description=models.CharField(max_length=2000)
    Price=models.FloatField()
    Image=models.CharField(max_length=3000)