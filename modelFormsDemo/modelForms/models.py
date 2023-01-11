from django.db import models

# Create your models here.
class Project(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    name = models.CharField()
    assinedTo = models.CharField()
    priority = models.IntegerField()