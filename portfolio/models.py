from django.db import models

# Create your models here.

class PortfolioQueryset(models.query.QuerySet):
    def publish(self):
        return self.filter(is_active=True)

class PortfolioManager(models.Manager):
    def get_queryset(self):
        return PortfolioQueryset(self.model, using=self._db)

    def publish(self):
        return self.get_queryset().publish()

class Portfolio(models.Model):
    title           = models.CharField(max_length=255)
    slug            = models.CharField(max_length=255)
    image           = models.ImageField(upload_to='uploads/portfolio')
    description     = models.TextField(null=True, blank=True)
    ext_link        = models.CharField(max_length=255, null=True, blank=True)
    start_date      = models.DateField()
    end_date        = models.DateField()
    created_date    = models.DateField(auto_now_add=True)
    is_active       = models.BooleanField(default=True)

    objects = PortfolioManager()

    def __str__(self):
        return self.title
