from rest_framework import serializers
from .models import Rating


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(choices=Rating.choices, required=False)
    synopsis = serializers.CharField(required=False)
    added_by = serializers.DateTimeField(read_only=True)
