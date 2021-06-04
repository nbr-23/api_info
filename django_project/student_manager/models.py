from django.db import models
from django.db.models.base import Model

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()


class Lesson(model.Model):
    name = models.CharField(max_length=30)
    teacher = models.CharField(max_length=30)

class School:
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    year = models.IntegerField(max_length=30)
    

    