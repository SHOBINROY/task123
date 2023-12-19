from django.contrib import auth, messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.

def register(request):

    if request.method == 'POST':
        name = None
        email = None
        password = None
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password']
        if password == password1:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('register')
            elif User.objects.filter(password=password).exists():
                messages.info(request, 'password not matching')
                return redirect('register')

            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.save()
                print("user created")
                return redirect('login')

        else:
            messages.info(request, 'password arent matching')
            return redirect('register')

    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
     auth.logout(request)
     return  redirect('/')
