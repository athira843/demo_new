from django.contrib import admin

from app1.models import Menuitem,Menu

# Register your models here.

admin.site.register(Menu)
admin.site.register(Menuitem)