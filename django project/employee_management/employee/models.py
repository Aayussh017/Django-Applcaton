# models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.age} - {self.department}"
