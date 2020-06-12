from django.db import models


# Create your models here.

class Contact_usr(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=100)
    message = models.TextField()
