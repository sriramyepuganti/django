from django.db import models

# Create your models here.

class InfoTable(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    img = models.ImageField(default="null")
     
