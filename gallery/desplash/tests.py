from django.test import TestCase
from . models import Image, Category, Location

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.test_location = Location(location="malindi")

    def test_saving_location(self):
        self.test_location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_deleting_locations(self):
        self.test_location = Location(location="Eastleigh")
        self.test_location.save_locations()
        self.test_location.delete_locations()
        locations = Location.objects.all()
        self.assertTrue(len(locations) < 1)

class ImageTestClass(TestCase):
    def setUp(self):

        self.test_image = Image(image="IMG",
                                image_name="Test",
                                description="Bla bla bla",
                                )
        self.test_image.save()

    def test_saving_image(self):
        self.test_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.test = Category(category="people")
