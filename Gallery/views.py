from django.shortcuts import render

# Create your views here.

## welcome view
def welcome(request):
    return render(request, "welcome.html")


## index view
def index(request):
    return render(request, "index.html")

