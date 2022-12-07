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


class MovieOrder(models.Model):
    user = models.ForeignKey(User, verbose_name="movie_order", on_delete=models.CASCADE)
    movie = models.ForeignKey(
        Movie, verbose_name="movie_order", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = models.DateTimeField(auto_now_add=True)
