from django.db import models

# Create your models here.
class teacher(models.Model):
    firstname = models.CharField( max_length=20 )
    lastname = models.CharField( max_length=20 )
    teacher_id = models.IntegerField()
    mobile = models.IntegerField()
class student(models.Model):
    firstname = models.CharField( max_length=20 )
    lastname = models.CharField( max_length=20 )
    student_id = models.IntegerField()
    mobile = models.IntegerField()

