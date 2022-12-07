from rest_framework.views import APIView, Request, Response, status

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmOrReadOnly

from movies.serializers import MovieOrderSerializer, MovieSerializer
from .models import Movie


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAdmOrReadOnly]

    def get(self, request):
        serializer = MovieSerializer(Movie.objects.all(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(**{"user": request.user})

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieByIdView(APIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAdmOrReadOnly]

    def get(self, request, movie_id):
        try:
            serializer = MovieSerializer(Movie.objects.get(id=movie_id))
        except Movie.DoesNotExist:
            return Response(
                {"detail": f"Movie by id {movie_id} does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, movie_id):
        try:
            movie_delete = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"detail": f"Movie by id {movie_id} does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )

        movie_delete.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrder(APIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"detail": f"Movie by id {movie_id} does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = MovieOrderSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(**{"user": request.user, "movie": movie})

        return Response(serializer.data, status=status.HTTP_201_CREATED)
