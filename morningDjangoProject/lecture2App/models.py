from django.db import models
from django.utils import timezone

# Create your models here.
class Chair(models.Model):
    leg = models.IntegerField(default=0)
    purpose = models.CharField(default="", max_length=1000)
    purchaseTime = models.DateTimeField(default=timezone.now())
