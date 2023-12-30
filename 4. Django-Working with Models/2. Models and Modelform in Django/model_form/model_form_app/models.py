from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    class_name = models.IntegerField(default=7)

    def __str__(self) -> str:
        return f"Name: {self.name}"