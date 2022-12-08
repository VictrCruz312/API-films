from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.permissions import IsAdmOrIsUser
from .models import User
from .serializers import UserSerializer
import ipdb


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
        try:
            serializer = UserSerializer(User.objects.get(id=user_id))
        except User.DoesNotExist:
            return Response(
                {"detail": f"User by id {user_id} does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(serializer.data, status=status.HTTP_200_OK)
