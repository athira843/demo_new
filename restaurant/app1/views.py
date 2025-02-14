from django.shortcuts import render

from django.http import HttpResponse
from app1.forms import Itemform
from django.shortcuts import render, redirect

from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from app1.models import Menu
from app1.models import Menuitem

class Home(TemplateView):
    model= Menu
    template_name = "home.html"

from django.urls import reverse_lazy
class Addmenu(CreateView):
    model = Menu
    fields = ['name','description']
    template_name = "addmenu.html"
    success_url = reverse_lazy('home')

class Additems(CreateView):
    model = Menuitem
    #fields = ['name','price','menu','is_vegetarian']
    form_class = Itemform
    template_name = "addmenu.html"
    success_url = reverse_lazy('home')


class Menulist(ListView):
    model=Menu
    template_name ="menulist.html"
    context_object_name="menu"



class Menudetails(DetailView):
    model=Menu
    template_name = "menudetails.html"
    context_object_name = "menu"

from django.contrib.auth.models import User
class Register(CreateView):

    model=User
    fields = ['username','password','email','first_name','last_name']
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        u=form.cleaned_data['username']
        p=form.cleaned_data['password']
        e=form.cleaned_data['email']
        f=form.cleaned_data['first_name']
        l=form.cleaned_data['last_name']
        u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
        u.save()
        return redirect('home')


from django.contrib.auth import authenticate,login,logout

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('home')

        else:
              return HttpResponse("Invalid user credentials")

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return user_login(request)


class PriceUpdate(UpdateView):
    model = Menuitem
    fields = ['price']
    template_name = 'addprice.html'
    success_url = reverse_lazy('home')