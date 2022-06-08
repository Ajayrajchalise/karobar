from cgi import print_exception
from email.mime import image
import imp
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class productDetailsVehicles(models.Model):
    Ad_id= models.IntegerField(max_length=10, null=False , blank=False)
    Title = models.TextField(max_length=30, null=False, blank=False)
    Description= models.TextField(max_length=100, null=True, blank=True)
    Price= models.IntegerField()
    Location = models.TextField()
    
    Image = models.ImageField()
    

    


    def __str__(self):
        return self.Title


    @property
    def imageurl(self):
        try:
            url = self.Image.url
        except:
            url=''
        return url

