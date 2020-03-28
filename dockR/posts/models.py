from django.db import models

class feed(models.Model):
    id = models.IntegerField(primary_key=True)
    name= models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    description = models.TextField()
