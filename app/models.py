from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    roll = models.IntegerField()
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    faculty_choices = (
        ('Management','Management'),
        ('Science & Technology','Science & Technology'),
    )
    marks = models.IntegerField()
    programme_choices = (
        ('BBA','BBA'),
        ('BCA','BCA'),
        ('MCA','MCA'),
        ('MBA','MBA'),
    )
    faculty = models.CharField(max_length=50, choices=faculty_choices)
    programme = models.CharField(max_length=20, choices=programme_choices)


    def __str__(self):
        return f'{self.name}- {self.phone}'
