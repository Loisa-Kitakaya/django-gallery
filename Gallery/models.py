from django.db import models

# Create your models here.

## Images
class Images(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=200)
    location = models.ForeignKey("Location", on_delete=models.CASCADE,)
    category = models.ForeignKey("Category", on_delete=models.CASCADE,)

    def __str__(self):
        return self.image_name


## Location
class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location


## Category
class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


"""
methods to save, delete, and retrieve data from the database
"""

def show_all():
    image_objects = Images.objects.all()

    return image_objects

def save_image(picture, name, description, pic_location, pic_category):
    image_object = Images(image = picture, image_name = name, image_description = description, location = pic_location, category = pic_category)
    
    image_object.save()

def get_image_by_id(pic_id):
    image_object = Images.objects.get(pk=pic_id)

    return image_object

@classmethod
def delete_image(cls):
    pass

@classmethod
def filter_by_category(cls, category):
    pass

@classmethod
def filter_by_location(cls, location):
    pass
