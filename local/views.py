from django.shortcuts import render
from django import forms
from django.http import HttpResponse
# Create your views here.



# page for authentication 
def auth(request):
    return render(request, 'local/auth.html')


# page for menu + all orders acceptance + calculate bills
def orders(request):
    return render(request, 'local/order.html')


# page for adding or deleting any items from the  owners database
def settings(request):
    return render(request, 'local/settings.html')


# page for listing past orders
def history(request):
    return render(request, 'local/history.html')


# page to render when offline
def offline(request):
    return render(request, 'local/offline.html')


# page to render when content is not loaded
def error(request, error):
    return render(request, 'local/error.html',{
        'error': error,
    })
