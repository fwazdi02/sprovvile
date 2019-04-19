import os
import random
from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from myprofile.models import Myprofile


class Config(Site):
    site            = models.CharField(max_length=255, blank=True, null=True)      
    keywords        = models.CharField(max_length=255, blank=True, null=True)     
    google_maps     = models.TextField(blank=True, null=True) 
    logo            = models.ImageField(upload_to='uploads/config', null=True, blank=True)        
    icon            = models.ImageField(upload_to='uploads/config', null=True, blank=True)        
    about           = models.TextField(blank=True, null=True)       
    metatext        = models.TextField(blank=True, null=True)    
    myprofile       = models.ForeignKey(Myprofile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.site

    def save(self):
        # Site model use cache 
        Config.objects.clear_cache()
        super(Config, self).save()
