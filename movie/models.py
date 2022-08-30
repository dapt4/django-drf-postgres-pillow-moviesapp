from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=30)
    image = models.CharField(max_length=250)
