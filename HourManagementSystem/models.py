from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    workingHours = models.IntegerField()

    def __str__(self):
        return self.name
