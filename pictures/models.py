from django.db import models

# Create your models here.
class Editor(models.Model):
    '''
    Editor model to show the user who is to upload the pictures
    '''
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']    

    def save_editor(self):
        self.save()

    def delete_editor(self):
        Editor.objects.all().delete()        

class Location(models.Model):
    '''
    Shows the location of the image
    '''
    name = models.CharField(max_length =30)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name

class Category(models.Model):
    '''
    shows the category of the pictures
    '''
    name = models.CharField(max_length =30, verbose_name = 'name')

    def __str__(self):
        return self.name 

    class Meta:
            verbose_name = "category"
            verbose_name_plural = "categories"

class Image(models.Model):
    '''
    Shows the grid of images to be uploaded
    '''
    image = models.ImageField(upload_to = 'image/')
    image_name = models.CharField(max_length =20)
    image_description = models.TextField(max_length =50)
    image_location = models.ForeignKey('Location', null=True, unique=False, blank=True)
    image_category = models.ForeignKey('Category', null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    @classmethod
    def search_by_image_category(cls,search_term):
        pictures = cls.objects.filter(image_category__icontains=search_term)
        return pictures
    



