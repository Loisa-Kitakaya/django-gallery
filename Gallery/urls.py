from django.urls import path
from . import views

# URLconf

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("gallery/", views.index, name="index"),
]
