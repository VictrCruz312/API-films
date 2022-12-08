from rest_framework.views import APIView, Request, Response, status

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions, pagination
from users.permissions import IsAdmOrReadOnly

from movies.serializers import MovieOrderSerializer, MovieSerializer
from .models import Movie
from django.shortcuts import get_object_or_404


class MovieView(APIView, pagination.PageNumberPagination):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAdmOrReadOnly]

    def get(self, request):
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request, view=self)

        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(**{"user": request.user})

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieByIdView(APIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAdmOrReadOnly]

    def get(self, request, movie_id):
        serializer = MovieSerializer(get_object_or_404(Movie, id=movie_id))

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, movie_id):
        movie_delete = get_object_or_404(Movie, pk=movie_id)

        movie_delete.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrder(APIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieOrderSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(**{"user": request.user, "movie": movie})

        return Response(serializer.data, status=status.HTTP_201_CREATED)
