from django.contrib import admin

# Register your models here.
from .models import Newitem, Newlabel

admin.site.register(Newitem)
admin.site.register(Newlabel)
