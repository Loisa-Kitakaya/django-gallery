from django import forms

# form models here
class ImageUpload(forms.Form):

    image_upload = forms.ImageField()
    image_name_upload = forms.CharField(max_length=30)
    image_description_upload = forms.CharField(max_length=200)
    location_upload = forms.CharField(max_length=30)
    category_upload = forms.CharField(max_length=30)


class SearchImages(forms.Form):

    search = forms.CharField(max_length=30)

