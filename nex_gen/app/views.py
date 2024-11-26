from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def user_home(req):
    return render(req,'home.html')

def user_about(req):
    return render(req,'about.html')

def user_contact(req):
    if req.method=='POST':
          name=req.POST['name']
          email=req.POST['email']
          message=req.POST['message']
          data=Std.objects.create(name=name,email=email,message=message)
          data.save()
          return redirect(user_contact)
    return render(req,'contacts.html')

def course_list(req):
    courses = Course.objects.all()  
    return render(req, 'course.html', {'courses': courses})

