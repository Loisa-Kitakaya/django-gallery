from django.urls import path
from . import views

# URLconf
app_name = "Gallery"
urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("gallery/", views.index, name="index"),
    path("upload/", views.image_upload, name="image_upload"),
    path("search/", views.search_image, name="search_image"),
]
