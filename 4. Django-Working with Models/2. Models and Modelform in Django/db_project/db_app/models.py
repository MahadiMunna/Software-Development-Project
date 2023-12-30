from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    class_name = models.IntegerField(default=6)

    def __str__(self):
        return f"Name: {self.name}, Roll: {self.roll}"
    