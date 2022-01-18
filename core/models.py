from django.db import models

# Create your models here.

class Outlet(models.Model):
    name = models.CharField(max_length=200)
    discounts = models.BooleanField(default=False)
    bonuses = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    gps = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
