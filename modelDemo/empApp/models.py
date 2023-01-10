from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.CharField(max_length=35)
    def __str__(self):
        return self.firstName

class Score(models.Model):
    score = models.IntegerField()

    def __str__(self):
        return str(self.score)