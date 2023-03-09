from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=100)
    movie_releaseDate = models.DateField()
    movie_rating = models.IntegerField(max_length=1)
    
    def __str__(self):
        return self.movie_title
