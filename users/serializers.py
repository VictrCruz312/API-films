from rest_framework import serializers
from .models import User
import ipdb


class UserSerializer(serializers.Serializer):
    id: serializers.CharField(read_only=True)
    username: serializers.CharField()
    email: serializers.EmailField()
    birthdate: serializers.DateField(allow_null=True, default="")
    first_name: serializers.CharField()
    last_name: serializers.CharField()
    password: serializers.CharField()
    is_employee: serializers.BooleanField(default=False)
    is_superuser: serializers.BooleanField(read_only=True)

    def validate_email(self, obj):
        get_user_by_email = User.objects.get(email=obj)

        if get_user_by_email:
            raise serializers.ValidationError("email already registered.")

        return obj

    def validate_username(self, obj):
        get_user_by_username = User.objects.get(username=obj)

        if get_user_by_username:
            raise serializers.ValidationError("username already taken.")

        return obj

    def create(self, validated_data):

        # if validated_data["is_employee"]:
        #     return User.objects.create_superuser(validated_data)

        return User.objects.create_user(**validated_data)
