from django.urls import path
from movielist import views

urlpatterns = [
    path("", views.MoviesView.as_view(), name='movielist'),
    path("<int:id>", views.MovieDetails.as_view(), name='moviedetail'),
    path("search",views.Search.as_view(),name='search'),
]
