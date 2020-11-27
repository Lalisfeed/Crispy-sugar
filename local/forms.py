from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# user forms

class NewLoginForm(forms.Form):
    key_mail = forms.CharField(max_length=128, required=True)
    key_code = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'stame'}))


class NewSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

    # keys_fname = forms.CharField(max_length=64, required=True)
    # keys_lname = forms.CharField(max_length=64, required=True)
    # keys_mail = forms.EmailField(max_length=128, required=True)
    # keys_code = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'pname'}))


class NewLabelField(forms.Form):
    new_item_label = forms.CharField(max_length=32, required=True)



class NewItemField(forms.Form):
    # labels and choices for new item field
    Veg_choices = [('Veg', 'Veg'),
                   ('Non', 'Non-Veg')]
    new_item_name = forms.CharField(max_length=64, required=True)
    new_item_price = forms.IntegerField(min_value=0, max_value=100000, required=True)
    new_item_label = forms.Select()
    new_veg_label = forms.ChoiceField(choices=Veg_choices, widget=forms.RadioSelect())


class NewDeleteField(forms.Form):
    del_item_name = forms.CharField(max_length=64, required=True)


class NewDelLabelField(forms.Form):
    del_label_name = forms.CharField(max_length=64, required=True)


class NewOrderField(forms.Form):
    quantity = forms.IntegerField(min_value=0, max_value=10,required=True)