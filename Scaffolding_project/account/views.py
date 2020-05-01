from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User,Group
from .form import CreateUserForm
from django.contrib.auth.views import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from users.decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
# Create your views here.
@unauthenticated_user
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
            user=form.save()
            group = Group.objects.get(name='user')
            user.groups.add(group)
            messages.success(request,"User Successfully created")
            return redirect('dashboard')
    context={
        'form':form
                }
    return render(request,'account/register.html',context)
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/account')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })