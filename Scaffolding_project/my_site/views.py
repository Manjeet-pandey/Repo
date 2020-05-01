from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.decorators import allowed_users

# Create your views here.

def dashboard(request):
    
    return render(request,'dashboard.html',{})
