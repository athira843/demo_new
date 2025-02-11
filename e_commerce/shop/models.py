from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='media/images',blank=True,null=True)
    description=models.TextField()

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField('media/products',blank=True,null=True)
    price = models.IntegerField()
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")


    def __str__(self):
        return self.name

