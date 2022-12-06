from rest_framework import serializers
from .models import User
import ipdb


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    birthdate = serializers.DateField(required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField(required=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def validate_email(self, obj):

        get_user_by_email = User.objects.filter(email=obj).exists()

        if get_user_by_email:
            raise serializers.ValidationError("email already registered.")

        return obj

    def validate_username(self, obj):
        get_user_by_username = User.objects.filter(username=obj).exists()

        if get_user_by_username:
            raise serializers.ValidationError("username already taken.")

        return obj

    def create(self, validated_data):
        if "is_employee" in validated_data:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)
