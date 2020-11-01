from django.shortcuts import render
from django import forms
from django.http import HttpResponse
# Create your views here.


# user forms

class NewLoginForm(forms.Form):
    key_mail = forms.EmailField(max_length=50, required=True)
    key_code = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'stame'}))


class NewSignUpForm(forms.Form):
    keys_fname = forms.CharField(max_length=50, required=True)
    keys_lname = forms.CharField(max_length=50, required=True)
    keys_mail = forms.EmailField(max_length=50, required=True)
    keys_code = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'pname'}))


# page for authentication 
def auth(request):
    return render(request, 'local/auth.html', {
        "loginForm": NewLoginForm(),
        "nextForm": NewSignUpForm()
    })


# page for menu + all orders acceptance + calculate bills
def menu(request):
    return render(request, 'local/menu.html')


# page for adding or deleting any items from the  owners database
def settings(request):
    return render(request, 'local/settings.html')


# page for listing past orders
def orders(request):
    return render(request, 'local/orders.html')


# page for viewing profile and request option for deleting account
def profile(request):
    return render(request, 'local/profill.html')


# page to render when offline
def offline(request):
    return render(request, 'local/offline.html')


# page to render when content is not loaded
def error(request, error):
    return render(request, 'local/error.html',{
        'error': error,
    })
