"""
URL configuration for e_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
app_name='shop'
urlpatterns = [
path('',views.Categories.as_view(),name="home"),
path('product_page/<int:pk>',views.Categorydetails.as_view(),name="product_page"),
path('product_page',views.Productlist.as_view(),name="product_page"),
path('product_details/<int:pk>',views.Productdetails.as_view(),name="product_details"),
path('register',views.register,name="register"),
path('login',views.user_login,name="login"),
path('logout',views.user_logout,name="logout"),
    path('add_categories',views.Addcategory.as_view(),name="add_categories"),

#path('addproduct',views.Addproduct.as_view(),name="addproduct"),
path('add_products',views.addproducts,name="add_products"),

path('addstock/<int:pk>',views.Stockupdate.as_view(),name="addstock"),

]
