from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=10)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    
    CHOICES = [('1','One'),('2','Two'),('3','Three'),('4','Four'),('5','Five')]
    rating = models.CharField(max_length=10,choices=CHOICES)

    def __str__(self) -> str:
        return f"{self.album_name} by {self.musician.first_name}"