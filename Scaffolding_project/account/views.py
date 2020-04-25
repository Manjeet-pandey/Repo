from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .form import CreateUserForm
from django.http import HttpResponse
# Create your views here.
def loginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Login successful ! Welcome")
            return redirect('dashboard')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('login')
    else:
        return render(request,'account/loginPage.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    form=CreateUserForm()
    if request.method=='POST':
         form=CreateUserForm(request.POST)
         if form.is_valid():            
            form.save()
            messages.success(request,"User Successfully created")
            return redirect('dashboard')
    context={
        'form':form
                }
    return render(request,'account/register.html',context)
