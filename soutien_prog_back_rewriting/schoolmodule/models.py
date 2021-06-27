from django.db import models

# Create your models here.
class SchoolModule(models.Model):
    module_name = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.module_name
