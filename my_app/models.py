from django.db import models

# Create your models here.

class Data(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=2560)
    text = models.TextField()