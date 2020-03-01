from django.urls import path
from . import views

# URLconf

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("gallery/", views.index, name="index"),
    path("upload/", views.image_upload, name="image_upload"),
]
