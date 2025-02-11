from lib2to3.fixes.fix_input import context
from symtable import Class

from django.contrib.auth.management.commands.changepassword import UserModel
from django.shortcuts import render, redirect

from django.views.generic import TemplateView, CreateView, ListView, DetailView

from app1.models import School

from app1.forms import Schoolform




# Create your views here.
class Home(TemplateView):
    model=School
    template_name = "home.html"

from django.urls import reverse_lazy
class Addschool(CreateView):
    model = School
    #fields = ['name','location','principal']
    form_class = Schoolform
    template_name = "addschool.html"
    success_url = reverse_lazy('home')

from app1.models import Student
class Addstudent(CreateView):

    model=Student
    fields=['name','age','school']
    template_name = "addstudent.html"
    success_url = reverse_lazy('home')


class Schoollist(ListView):
    model=School
    template_name ="schoollist.html"
    context_object_name="school"
    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(location="kannur")
    #     return queryset

class Studentlist(ListView):
    model=Student
    template_name ="studentlist.html"
    context_object_name="students"
    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(school__location="kannur")#foreign key field school.To compare location we use school__location
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(name__icontains="th")
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(age__gt=15)
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(age__lt=16)
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(name__startswith="v")
    #     return queryset


    #get_content_data()
    def get_context_data(self):
        context=super().get_context_data()
        context['name']='devan'
        context['school']=School.objects.all()
        return context


class Schooldetail(DetailView):
    model=School
    template_name = "schooldetail.html"
    context_object_name = "school"





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

from django.contrib.auth.views import LoginView
class Login(LoginView):
    template_name ="login.html"


from django.contrib.auth import logout
from django.views.generic import View
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('home')


