from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import RedirectView

urlpatterns = [
    path('movie-list',views.MovieList.as_view()),
    path('add-movie',views.addMovie),
    path('movie-detail/<int:id>',views.movie_detail),
    path('rdt',RedirectView.as_view(url = "http://www.google.com") , name= "go-to-this-link")
]
urlpatterns = format_suffix_patterns(urlpatterns)