from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        username = request.POST['uname']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password=request.POST['pswd']
        cpassword = request.POST['cpswd']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return  render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already used")
                return render(request,'register.html')
            else:
                user = User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save()
                messages.info(request,"Registered succesfully")
                print("User Registered")
                return render(request,'login.html')

        else:
            messages.info(request,"Password missmatch")
            return render(request,'register.html')

        return redirect('/')

    return  render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
                auth.login(request,user)
                messages.info(request, "successfully logged in")
                return render(request,'store.html')
        else:
                messages.info(request,"Invalid login credentials")
                return render(request,'login.html')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')