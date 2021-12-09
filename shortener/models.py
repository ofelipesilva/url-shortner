from django.db import models
from django.urls import reverse

# Create your models here.
class URL(models.Model):
    link = models.CharField(max_length=99999)
    uuid = models.CharField(max_length=10)

    def get_absolute_urls(self):
        return reverse('shortener:create', kwargs={'url': self.link})