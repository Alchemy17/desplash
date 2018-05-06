from django.test import TestCase
from . models import Image, Category, Location

# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):

        # Category
        self.test_category = Category(category="food")
        self.test_category.save()
    
        # Location
        self.test_location = Location(location="malindi")
        self.test_location.save()
    
    def test_deleting_image(self):
        self.test_image = Image(location="kisumu")
        self.test_image.save_image()
        self.test_image.delete_locations()
        locationss = Image.objects.all()
        self.assertTrue(len(locationss) < 1)
    

class CategoryTestClass(TestCase):
    def setUp(self):
        self.test = Category(category="people")