from django.test import TestCase
from .models import Editor,Image,Location,Category

# Create your tests here.
class EditorTestClass(TestCase):
    '''
    Testing the Editor class
    '''

    #setup method
    def setUp(self):
        self.pius= Editor(first_name = 'Pius', last_name = 'Clark', email = 'pitchclark@gnmail.com')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pius,Editor)) 

    #Testing save method
    def test_save_method(self):
        self.pius.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)  

    #Testing Delete method
    def test_delete_method(self):
        self.pius.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) ==0)

    def tearDown(self):
        Editor.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()


class LocationTestClass(TestCase):
    '''
    Testing the Location model
    '''

    def setUp(self):
         self.location = Location(name= 'Ngong')

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))     

    # Testing save method
    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.save_location()
        self.location.delete_location()    
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

class CategoryTestClass(TestCase):
    '''
    Testing the category class
    '''
    #Testing the save method
    def setUp(self):
         self.category = Category(name= 'Travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))     

    # Testing save method
    def test_save_method(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.category.save_category()
        self.category.delete_category()    
        category = Category.objects.all()
        self.assertTrue(len(category)==0)


class ImageTestClass(TestCase):
    '''
    Testing the Image class
    '''
    def setUp(self):
        self.image = Image()
    #Testing the save method
                








