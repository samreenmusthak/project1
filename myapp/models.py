from django.db import models
class users(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
