from django.db import models
from course.models import Course


class Participant(models.Model):
    name = models.CharField(max_length=40)
    mail = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.mail
