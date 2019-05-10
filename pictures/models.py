from django.db import models

# Create your models here.
class Editor(models.Model):
    '''
    Editor model to show the user who is to upload the pictures
    '''
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class Location(models.Model):
    '''
    Shows the location of the image
    '''
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Category(models.Model):
    '''
    shows the category of the pictures
    '''
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name         

class Image(models.Model):
    '''
    Shows the grid of images to be uploaded
    '''
    image = models.ImageField()
    image_name = models.CharField(max_length =20)
    image_description = models.TextField(max_length =50)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    



