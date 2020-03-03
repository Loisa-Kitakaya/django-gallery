from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

## welcome view
def welcome(request):
    return render(request, "welcome.html")


## index view
def index(request):

    all_images = show_all()

    return render(request, "index.html", {"all_images" : all_images})


## image upload view
def image_upload(request):

    if request.method == "POST":

        image_form = ImageUpload(request.POST, request.FILES)

        if image_form.is_valid():

            picture = image_form.cleaned_data["image"]
            name = image_form.cleaned_data["image_name"]
            description = image_form.cleaned_data["image_description"]
            pic_location = image_form.cleaned_data["image_location"]
            pic_category = image_form.cleaned_data["image_category"]

            save_image(picture, name, description, pic_location, pic_category)

    return redirect("index")


## search_images view
def search_image(request):

    if request.method == "GET":

        search_form = SearchImages(request.POST, request.FILES)

        if search_form.is_valid():

            pic_id = search_form.cleaned_data["search"]

            search_result = get_image_by_id(pic_id)

    return render(request, "index.html", {"search_result" : search_result})
