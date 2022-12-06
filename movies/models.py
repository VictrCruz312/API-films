from django.db import models
from users.models import User


class Rating(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG13"
    R = "R"
    NC17 = "NC17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(max_length=20, choices=Rating.choices, default=Rating.G)
    synopsis = models.TextField(null=True)

    user = models.ForeignKey(User, verbose_name="movies", on_delete=models.CASCADE)
