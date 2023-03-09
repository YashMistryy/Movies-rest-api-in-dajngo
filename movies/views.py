from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import  api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def showAllMovies(request , format=None):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies , many = True)
    return Response(serializer.data)


@api_view(['POST'])
def addMovie(request):
    # we'll be getting movie detail from the POST request and save it with the help of serializer
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def movie_detail(request , id , format=None):
    try:
        myMovie = Movie.objects.get(pk = id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if (request.method == "GET"):
        serializer = MovieSerializer(myMovie)
        return Response(serializer.data)
    elif(request.method == "PUT"):
        serializer = MovieSerializer(myMovie,data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.error_messages , status=status.HTTP_400_BAD_REQUEST)
    elif(request.method == "DELETE"):
        serializer = MovieSerializer(myMovie)
        myMovie.delete()
        return Response(serializer.data , status=status.HTTP_202_ACCEPTED)