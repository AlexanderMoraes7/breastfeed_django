from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import AccountsForm


def login_view(request : HttpRequest):        # <- type annotations
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, auth)
            return redirect('feed')
        else:
            login_form = (AuthenticationForm(request, data=request.POST))
    else:
        login_form = AuthenticationForm()
    
    return render(
        request,
        'login.html',
        {'login_form': login_form}
    )

def accounts_view(request : HttpRequest):
    if request.method == 'POST':
        form = AccountsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = AccountsForm()
        
    return render(
        request, 
        'accounts.html',
        {'accounts_form': form}
    )

def logout_view(request):
    logout(request)
    return redirect('login')

def account_recovery(request):
    return render(
        request,
        'account_recovery.html',
    )