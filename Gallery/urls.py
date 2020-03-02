from django.urls import path
from . import views

# URLconf
urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("gallery/", views.index, name="index"),
    path("upload/", views.imageupload, name="imageupload"),
    path("searchimage/", views.searchimage, name="searchimage"),
]
