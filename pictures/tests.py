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
         self.pius= Editor(first_name = 'Pius', last_name = 'Clark', email = 'pitchclark@gnmail.com')

    #Testing save method
    # def test_save_method(self):
    #     self.pius.save_location()
    #     location = Location.objects.all()
    #     self.assertTrue(len(location) > 0)

class CategoryTestClass(TestCase):
    '''
    Testing the category class
    '''
    #Testing the save method

class ImageTestClass(TestCase):
    '''
    Testing the Image class
    '''
    #Testing the save method
                








