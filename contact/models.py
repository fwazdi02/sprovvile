from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    message = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


