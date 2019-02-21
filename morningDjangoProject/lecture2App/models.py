from django.db import models
from django.utils import timezone

# Create your models here.
class Chair(models.Model):
    leg = models.IntegerField(default=0)
    purpose = models.CharField(default="", max_length=1000)
    purchaseTime = models.DateTimeField(default=timezone.now())

# name, age, and birthday attributes

class Person(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField(default=0)
    birthday = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name