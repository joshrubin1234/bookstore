from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=False,null=False, default='')
    email = models.EmailField(blank=False,null=False, default='')
    address = models.CharField(max_length=100,blank=False,null=False, default='') 

    def __str__(self):
        return self.username

    