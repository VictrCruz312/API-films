from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdmOrReadOnly


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAdmOrReadOnly]

    def get(self, request):
        ...

    def post(self, request):
        ...


class MovieByIdView(APIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAdmOrReadOnly]

    def get(self, request, movie_id):
        ...

    def delete(self, request, movie_id):
        ...
