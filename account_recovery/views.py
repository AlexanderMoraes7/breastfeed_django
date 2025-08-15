from django.shortcuts import render

def account_recovery_view(request):
    return render(
        request,
        'account_recovery.html',
    )