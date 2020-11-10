from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.


# user forms

class NewLoginForm(forms.Form):
    key_mail = forms.EmailField(max_length=128, required=True)
    key_code = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'stame'}))


class NewSignUpForm(forms.Form):
    keys_fname = forms.CharField(max_length=64, required=True)
    keys_lname = forms.CharField(max_length=64, required=True)
    keys_mail = forms.EmailField(max_length=128, required=True)
    keys_code = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'pname'}))


class NewLabelField(forms.Form):
    new_item_label = forms.CharField(max_length=32, required=True)

# labels and choices for new item field
Veg_choices = [('0', 'Veg'),
               ('1', 'Non-veg')]
 
class NewItemField(forms.Form):
    new_item_name = forms.CharField(max_length=64, required=True)
    new_item_price = forms.IntegerField(min_value=0, max_value=100000, required=True)
    new_item_label = forms.Select()
    new_veg_label = forms.ChoiceField(
        choices=Veg_choices, widget=forms.RadioSelect())


class NewDeleteField(forms.Form):
    del_item_name = forms.CharField(max_length=64, required=True)


# page for authentication 
def auth(request):
    return render(request, 'local/auth.html', {
        "loginForm": NewLoginForm(),
        "nextForm": NewSignUpForm()
    })


# page for menu + all orders acceptance + calculate bills
def menu(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('local:auth'))
    return render(request, 'local/menu.html')


# page for adding or deleting any items from the  owners database
def settings(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('local:auth'))

    return render(request, 'local/settings.html', {
        "labelForm": NewLabelField(),
        "itemForm": NewItemField(),
        "delForm": NewDeleteField(),
    })


# page for listing past orders
def orders(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('local:auth'))
    return render(request, 'local/orders.html')


# page for viewing profile and request option for deleting account
def profile(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse('local:auth'))
    return render(request, 'local/profill.html')



# page to redirect user on logout 
def noauth(request):
    logout(request)
    return render(request, "local/logout.html")



# page to render when offline
def offline(request):
    return render(request, 'local/offline.html')


# page to render when content is not loaded
def error(request, error):
    return render(request, 'local/error.html',{
        'error': error,
    })
