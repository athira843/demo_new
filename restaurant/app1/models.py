from django.db import models

# Create your models here.


class Menu(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()

    def __str__(self):
        return self.name


class Menuitem(models.Model):

    name=models.CharField(max_length=30)
    price=models.IntegerField()
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE,related_name="menuitems")


