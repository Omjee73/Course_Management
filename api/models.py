from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to built-in auth user
    enrolled_courses = models.ManyToManyField(Course, related_name='students')
    age = models.IntegerField(null=True)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        user = self.user
        super().delete(*args, **kwargs)
        user.delete()
