# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    def delete(self, *args, **kwargs):
        # User ko deactivate karo
        if self.user:
            self.user.is_active = False
            self.user.save()
        super().delete(*args, **kwargs)
