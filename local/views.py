from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Newitem, Newlabel, Userslist
from passlib.hash import pbkdf2_sha256
# Create your views here.


# user forms

class NewLoginForm(forms.Form):
    key_mail = forms.CharField(max_length=128, required=True)
    key_code = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'stame'}))


class NewSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name","username", "email", "password1", "password2"]
        
    # keys_fname = forms.CharField(max_length=64, required=True)
    # keys_lname = forms.CharField(max_length=64, required=True)
    # keys_mail = forms.EmailField(max_length=128, required=True)
    # keys_code = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'pname'}))


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
def new(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("menu/")
    if request.method == "POST":
        form = NewSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'local/new.html', {
                'nextForm': NewSignUpForm(),
                'good': 'Signed Up Successfully'
            })
        else:
            return render(request, 'local/new.html', {
                'nextForm': form,
                'false_data': 'Invalid Data'
            })
    else:
        form = NewSignUpForm()
    return render(request, 'local/new.html', {
        'nextForm': form
        })

# page for authentication
def auth(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("menu/")
    if request.method == "POST":
        usermail = request.POST["key_mail"]
        passcode = request.POST["key_code"]

        user = authenticate(request, username=usermail, password=passcode)

        if user is not None:
            login(request, user)
            return render(request, "local/menu.html", {
                "user":user
            })
        else:
            return render(request, "local/auth.html", {
                "loginForm": NewLoginForm(),
                "message": "Invalid Credentials"
            })
        
    return render(request, 'local/auth.html', {
        "loginForm": NewLoginForm(),
    })

# page for menu + all orders acceptance + calculate bills
def menu(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('local:auth'))
    return render(request, 'local/menu.html')


# page for adding or deleting any items from the  owners database
def settings(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('local:auth'))

    if request.method == "POST":
        if request.POST.get('new_item_label'):
            save_label = Newlabel()
            label_options = Newlabel.objects.all()
            save_label.label_name = request.POST['new_item_label']
            save_label.save()
            return render(request, 'local/settings.html', {
                "labelForm": NewLabelField(),
                "itemForm": NewItemField(),
                "select_label": label_options,
                "delForm": NewDeleteField(),
            })

        if request.POST.get('new_item_name'):
            save_item = Newitem()
            save_item.item_name = request.POST['new_item_name']
            save_item.item_price = request.POST['new_item_price']
            save_item.save()
            return render(request, 'local/settings.html', {
                "labelForm": NewLabelField(),
                "itemForm": NewItemField(),
                "select_label": Newlabel.objects.all(),
                "delForm": NewDeleteField(),
            })

        if request.POST.get('del_item_name'): # still checking
            del_item = NewDeleteField()
            del_item.del_item_name = request.POST['del_item_name']
            Newitem.objects.filter(item_name=del_item).delete()
            return render(request, 'local/settings.html', {
                "labelForm": NewLabelField(),
                "itemForm": NewItemField(),
                "select_label": Newlabel.objects.all(),
                "delForm": NewDeleteField(),
            })
    else :  
        return render(request, 'local/settings.html', {
            "labelForm": NewLabelField(),
            "itemForm": NewItemField(),
            "select_label": Newlabel.objects.all(),
            "delForm": NewDeleteField(),
        })
    
    return render(request, 'local/settings.html', {
        "labelForm": NewLabelField(),
        "itemForm": NewItemField(),
        "select_label": Newlabel.objects.all(),
        "delForm": NewDeleteField(),
    })


# page for listing past orders
def orders(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('local:auth'))
    return render(request, 'local/orders.html')


# page for viewing profile and request option for deleting account
def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('local:auth'))
    return render(request, 'local/profill.html')



# page to redirect user on logout 
def noauth(request):
    logout(request)
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('local:auth'))
    return render(request, "local/logout.html")



# page to render when offline
def offline(request):
    return render(request, 'local/offline.html')


# page to render when content is not loaded
def error(request, error):
    return render(request, 'local/error.html',{
        'error': error,
    })
