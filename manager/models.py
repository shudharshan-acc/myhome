from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
class videos(models.Model):
    username = models.CharField(max_length=200, blank=True)
    vidname = models.CharField(max_length=200,blank=True)
    link = models.URLField(max_length=1000,blank=True)

    def __str__(self):
        return self.username
    
class inventory(models.Model):
    username = models.CharField(max_length=200, blank=True)
    item = models.CharField(max_length=200,blank=True)
    quan = models.IntegerField()
    units = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.username