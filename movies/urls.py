from django.urls import path
from movies.views import MovieView, MovieByIdView, MovieOrder

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieByIdView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrder.as_view()),
]
