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

            picture = image_form.cleaned_data["image_upload"]
            name = image_form.cleaned_data["image_name_upload"]
            description = image_form.cleaned_data["image_description_upload"]
            pic_location = image_form.cleaned_data["location_upload"]
            pic_category = image_form.cleaned_data["category_upload"]

            save_image(picture=picture, name = name, description = description, pic_location = pic_location, pic_category = pic_category)

    return redirect("index")


## search_images view
def search_image(request):

    if request.method == "GET":

        search_form = SearchImages(request.POST, request.FILES)

        if search_form.is_valid():

            pic_id = search_form.cleaned_data["search"]

            search_result = get_image_by_id(pic_id)

    return render(request, "index.html", {"search_result" : search_result})
