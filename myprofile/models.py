from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Myprofile(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE) 
    avatar          = models.ImageField(upload_to='uploads/profile')
    about_me        = models.TextField()
    address         = models.CharField(max_length=255, blank=True, null=True)     
    city            = models.CharField(max_length=255, blank=True, null=True)        
    zip_code        = models.CharField(max_length=255, blank=True, null=True)    
    phone_number    = models.CharField(max_length=255, blank=True, null=True) 
    fax             = models.CharField(max_length=255, blank=True, null=True)          
    facebook        = models.CharField(max_length=255, blank=True, null=True)     
    twitter         = models.CharField(max_length=255, blank=True, null=True)      
    instagram       = models.CharField(max_length=255, blank=True, null=True)    
    pinterest       = models.CharField(max_length=255, blank=True, null=True)
    github          = models.CharField(max_length=255, blank=True, null=True)
    gitlab          = models.CharField(max_length=255, blank=True, null=True)
    cv              = models.FileField(upload_to='uploads/profile')    

    def __str__(self):
        return "{}".format(self.user.username)

class Skill(models.Model):
    user            = models.ForeignKey(Myprofile, on_delete=models.CASCADE)
    title           = models.CharField(max_length=255)
    presentase      = models.PositiveIntegerField()
    max_presentase  = models.PositiveIntegerField()
    description     = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

