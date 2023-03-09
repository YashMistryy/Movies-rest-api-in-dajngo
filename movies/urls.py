from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('movie-list',views.showAllMovies),
    path('add-movie',views.addMovie),
    path('movie-detail/<int:id>',views.movie_detail)
]
urlpatterns = format_suffix_patterns(urlpatterns)