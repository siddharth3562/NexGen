from django.db import models

# Create your models here.

class Course(models.Model):
    cid = models.TextField()
    title = models.TextField()  # Name of the course
    description = models.TextField()  # Detailed course information
    duration = models.TextField()  # Course length
    fee = models.IntegerField()  # Cost of the course
    img=models.FileField()
    start_date = models.DateField()

class Std(models.Model):
    name=models.TextField()
    email=models.EmailField()
    message=models.TextField()
