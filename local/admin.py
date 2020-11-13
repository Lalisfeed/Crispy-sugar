from django.contrib import admin

# Register your models here.
from .models import Userslist, Newitem, Newlabel

admin.site.register(Userslist)
admin.site.register(Newitem)
admin.site.register(Newlabel)
