from django.urls import path
from cinema.views import (
    cinema_list_create,
    cinema_detail_retrieve_update_delete
)

app_name = "cinema"

urlpatterns = [
    path("movies/", cinema_list_create, name="cinema-list"),
    path("movies/", cinema_list_create, name="cinema-create"),
    path(
        "movies/<int:pk>/",
        cinema_detail_retrieve_update_delete,
        name="cinema-detail"
    ),
    path(
        "movies/<int:pk>",
        cinema_detail_retrieve_update_delete,
        name="cinema-update"
    ),
    path(
        "movies/<int:pk>",
        cinema_detail_retrieve_update_delete,
        name="cinema-delete"
    ),
]
