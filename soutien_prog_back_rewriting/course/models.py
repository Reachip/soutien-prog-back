from django.db import models
from django.contrib.auth.models import User
from schoolmodule.models import SchoolModule


class Course(models.Model):
    course_name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    starting_at = models.DateTimeField()
    link_to = models.CharField(max_length=255, default="https://discord.gg/")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    school_module = models.ForeignKey(SchoolModule, on_delete=models.CASCADE, null=True)
    ending_at = models.DateTimeField()

    def __str__(self):
        return f"{self.starting_at} - {self.ending_at}"
