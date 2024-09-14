from django.db import models

# Create your models here.
class Moviedata(models.Model):
    def __str__(self) -> str:
        return self.name
    name=models.CharField(max_length=200)
    duration=models.FloatField()
    rating=models.FloatField()
    gener=models.CharField(default='Comedy',max_length=100)
    poster=models.ImageField(upload_to='media/',default='media/None/Noimg.jpg')