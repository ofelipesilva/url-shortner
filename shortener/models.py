from django.db import models

# Create your models here.
class URL(models.Model):
    link = models.CharField(max_length=99999)
    uuid = models.CharField(max_length=10)
