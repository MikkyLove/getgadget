from django.shortcuts import redirect, render
from .models import Category
from .forms import CreateUserForm

# Create your views here.

def homepage(request):
    categories = Category.objects.all()
    context = {"product_category":categories}
    return render(request, 'eshop/homepage.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    
    context = {"form":form}
    return render(request, 'eshop/registration-form.html', context)

def login(request):
    return render(request, 'eshop/login-form.html')