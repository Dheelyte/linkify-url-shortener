from django.db import models
from django.urls import reverse

# Create your models here.

class Link(models.Model):
    link = models.URLField(max_length=256)
    short_link_id = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.short_link_id
    
    def get_absolute_url(self):
        return reverse('redirect', args=(self.short_link_id,))