from django.db import models

# Create your models here.

class Entity(models.Model):
    text = models.TextField(default='')
