from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request
from django.views.generic import ListView, DetailView,CreateView,UpdateView

from django.shortcuts import render

from shop.models import Category,Product
# Create your views here.
class Categories(ListView):
    model=Category
    template_name="category.html"
    context_object_name='item'

class Categorydetails(DetailView)  :
    model = Category
    context_object_name ='item'
    template_name ="product_page.html"

class Productlist(ListView):
    model = Product
    template_name="allproduct.html"
    context_object_name = 'products'


class Productdetails(DetailView):
    model=Product
    template_name = "product_details.html"
    context_object_name = 'products'



from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import  messages



# Create your views here.
def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        p1=request.POST['p1']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']




        if(p==p1):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
            return redirect('shop:home')


        else:


             return HttpResponse("password are not same")







    return render(request,'register.html')





from django.contrib.auth import authenticate,login,logout

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:home')

        else:
              return HttpResponse("Invalid user credentials")

    return render(request,'login.html')

from django.contrib.auth.decorators import login_required
@login_required()
def user_logout(request):
    logout(request)
    return user_login(request)


from django.urls import reverse_lazy
class Addcategory(CreateView):
    model = Category
    fields = ['name','description','image']
    template_name = "add_categories.html"
    success_url = reverse_lazy('shop:home')

# class Addproduct(CreateView):
#     model = Product
#     fields = ['name','description','image','price','stock','category']
#     template_name = "addproduct.html"
#     success_url = reverse_lazy('shop:home')


class Stockupdate(UpdateView):
    model = Product
    fields = ['stock']
    template_name = "addstock.html"
    success_url = reverse_lazy("shop:home")


def addproducts(request):
    if (request.method == "POST"):
        n = request.POST['n']
        i = request.FILES.get('i')
        d = request.POST.get('d')
        s=request.POST.get('s')
        p=request.POST.get('p')
        c=request.POST.get('c')

        ca=Category.objects.get(name=c)

        p=Product.objects.create(name=n,image=i,description=d,stock=s,price=p,category=ca)
        p.save()
        return redirect('shop:home')
    return render(request, 'add_products.html')

