from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    education = models.CharField(max_length=100)

    def __str__(self):
        return self.name