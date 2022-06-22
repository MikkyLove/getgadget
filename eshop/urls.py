from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.homepage, name='homepage'),
    path("sign-up", view=views.register, name='register'),
    path("login", view=views.login, name='login')
]