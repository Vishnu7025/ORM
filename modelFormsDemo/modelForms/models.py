from django.db import models

# Create your models here.
class Project(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    name = models.CharField(max_length=50)
    assinedTo = models.CharField(max_length=100)
    priority = models.IntegerField()
    def __str__(self) -> str:
        return self.name