from django.db import models

# Create your models here.

## Images
class Images(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="uploadimg/")
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

