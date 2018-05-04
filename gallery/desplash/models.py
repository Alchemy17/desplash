from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, blank=True)
    date_posted = models.DateTimeField(auto_now=True)

    @classmethod
    def searched(cls, query):
        result = cls.objects.filter(name__icontains=query).order_by('-date_posted').first()
        
        return result

    def __str__(self):
        return self.name
    
class Image(models.Model):
    image = models.ImageField(upload_to='gallery/', blank=True)
    image_url = models.TextField(blank=True)
    image_name = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=100, blank=True)
    date_posted = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)

    @classmethod
    def get_all(cls):
        images = cls.objects.order_by('-date_posted').all()
        return images

    @classmethod
    def get_Image_by_category(cls,category):
        images = cls.objects.filter(category=category).all()
        return images

