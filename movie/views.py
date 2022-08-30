from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
import uuid0

# Create your views here.
@api_view(['GET', 'POST'])
def movie(request):
    try:
        if request.method == 'GET':
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            image = Image.open(request.data['image'])
            name = str(request.data['image'])
            ext = name.split('.')
            link = 'static/' + str(uuid0.generate()) + '.' + ext[len(ext)-1]
            image.save(link)
            movie = Movie(
                title=request.data['title'],
                description=request.data['description'],
                year =request.data['year'],
                image=link
            )
            movie.save()
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        print(err)
        return Response({'error': 'internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT','DELETE'])
def edit_movie(request, id):
    try:
        movie = Movie.objects.get(id=id)
        if request.method == 'PUT':
            movie.title = request.data['title']
            movie.description = request.data['description']
            movie.year = request.data['year']
            image = Image.open(request.data['image'])
            image_name = str(request.data['image'])
            image_split = image_name.split('.')
            image_ext = image_split[len(image_split)-1]
            link = 'static/' + str(uuid0.generate()) + '.' + image_ext
            image.save(link)
            movie.image = link
            movie.save()
        elif request.method == 'DELETE':
            movie.delete()
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({'error': 'internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
