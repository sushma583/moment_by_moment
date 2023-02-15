from django.db import models

# Create your models here.

class user(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default=None)
    password = models.CharField(max_length=100, default=None)
    confirm_password = models.CharField(max_length=100, default=None)
