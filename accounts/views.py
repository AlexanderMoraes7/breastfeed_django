from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import AccountsForm

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