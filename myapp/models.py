from django.db import models

# Create your models here.

class track(models.Model):
    tittle=models.CharField(max_length=200)
    notes=models.TextField()