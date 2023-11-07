from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from collegeapp.models import course


# Create your views here.
def home(request):
    cor=course.objects.all()
    context={
       'course_list':cor

    }
    return render(request,'home.html',context)


# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password = request.POST['password']
#         # cpassword = request.POST['password1']
#         user = User.objects.create_user(username=username, password=password)
#         user.save();
#         print("user created")
#     return render(request, "login.html")
#
# def register(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password = request.POST['password']
#         cpassword = request.POST['password1']
#         if password==cpassword:
#             if User.objects.filter(username=username).exists():
#                messages.info(request,"username taken")
#                return redirect('login')
#
#             else:
#               user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
#               user.save();
#               return redirect('login')
#         else:
#              messages.info(request,"Password not matching")
#              return redirect('register')
#
#         return redirect('/')
#     return render(request,"register.html")
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/')
