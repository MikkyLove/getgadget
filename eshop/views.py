from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Category
from .forms import CreateUserForm
from .decorators import unauthenticated_user

# Create your views here.

@unauthenticated_user
def homepage(request):
    print(dir(request))
    print(dir(request.user))
    categories = Category.objects.all()
    context = {"product_category":categories}
    return render(request, 'eshop/homepage.html', context)

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data.get('username')
            messages.success(request, message="New User (%s) created" %(name))
            return redirect('login')
    
    context = {"form":form}
    return render(request, 'eshop/registration-form.html', context)

@unauthenticated_user
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user != None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Username or Password is incorrect")
    return render(request, 'eshop/login-form.html')

def userlogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request, pk=None):
    categories = Category.objects.all()
    context = {"product_category":categories}
    return render(request, 'eshop/dashboard.html', context)