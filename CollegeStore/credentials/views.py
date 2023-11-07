from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#            auth.login(request,user)
#            return redirect('/')
#         else:
#             messages.info(request,"invalid")
#             return redirect('login')
#
#     return render(request,"login.html")


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save();

    return render(request, "login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
    return render(request, "register.html")
    #     if password==cpassword:
    #         if User.objects.filter(username=username).exists():
    #            messages.info(request,"username taken")
    #            return redirect('register')
    #
    #         else:
    #           user=User.objects.create_user(username=username,password=password)
    #           user.save();
    #           return redirect('register')
    #     else:
    #          messages.info(request,"Password not matching")
    #          return redirect('register')
    #
    #     return redirect('/')
    # return render(request,"register.html")
    #

def form(request):
    return render(request,"form.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
