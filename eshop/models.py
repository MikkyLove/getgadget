from distutils.command.upload import upload
from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    catchphrase = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name}'

def resolve_image_upload_path(instance, filename):
    def ext(filename):
        return filename.split('.')[-1]
    return (f'get_gadget/{str(instance.name).replace(" ", "_")}.{ext(filename)}')

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=resolve_image_upload_path, null=True)

    def __str__(self):
        return f'{self.name} ({self.category})'

    