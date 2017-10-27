from django.db import models

# Create your models here.

class Entities(models.Model):
    text = models.TextField(default='')
