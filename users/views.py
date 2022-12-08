from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

from users.permissions import IsAdmOrIsUser
from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserByidView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmOrIsUser]

    def get(self, request, user_id):
        serializer = UserSerializer(get_object_or_404(User, id=user_id))

        return Response(serializer.data, status=status.HTTP_200_OK)
