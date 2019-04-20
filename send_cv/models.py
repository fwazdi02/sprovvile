from django.db import models

# Create your models here.

class EmailTemplate(models.Model):
    title = models.CharField(max_length=255)
    template = models.TextField()

class History(models.Model):
    email = models.EmailField()
    created_date = models.DateField(auto_now_add=True)