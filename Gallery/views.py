from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

## welcome view
def welcome(request):
    return render(request, "welcome.html")


## index view
def index(request):
    return render(request, "index.html")


## image upload view
def image_upload(request):

    if request.method == "POST":

        image_form = ImageUpload(request.POST, request.FILES)

        if image_form.is_valid():

            img = Images.objects.get(pk=id)
            loc = Location.objects.get(pk=id)
            cat = Category.objects.get(pk=id)

            img.image = image_form.cleaned_data["image"]
            img.image_name = image_form.cleaned_data["image_name"]
            img.image_description = image_form.cleaned_data["image_description"]
            img.save()

            loc.location = image_form.cleaned_data["location"]
            loc.save()

            cat.category = image_form.cleaned_data["category"]
            cat.save()

    return redirect("index")

