from rest_framework import serializers
from .models import Movie
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','movie_title','movie_releaseDate','movie_rating']