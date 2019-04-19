from django.db import models

# Create your models here.

# class EmailTemplate(models.Model):
#     template
#     title

class History(models.Model):
    email = models.EmailField()
    created_date = models.DateField(auto_now_add=True)