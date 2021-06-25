from django.db import models
from django.contrib.auth.models import User
from schoolmodule.models import SchoolModule


class Course(models.Model):
    description = models.CharField(max_length=255)
    starting_at = models.DateTimeField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    school_module = models.ForeignKey(SchoolModule, on_delete=models.CASCADE, null=True)
    ending_at = models.DateTimeField()

    def __str__(self):
        return f"{self.starting_at} - {self.ending_at}"
