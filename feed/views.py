from django.shortcuts import render
from django.http import HttpRequest

def feed_view(request : HttpRequest):
    return render(
        request,
        'feed.html',
    )