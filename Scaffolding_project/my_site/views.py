from django.shortcuts import render
from django.views import generic


# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html',{})
