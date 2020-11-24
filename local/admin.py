from django.contrib import admin

# Register your models here.
from .models import Newitem, Newlabel


class NewLabelAdmin(admin.ModelAdmin):
    list_display = ("id", "label_home", "label_name")


class NewItemAdmin(admin.ModelAdmin):
    list_display = ("id", "item_womb", "item_name", "item_label", "item_type", "item_price")


admin.site.register(Newitem, NewItemAdmin)
admin.site.register(Newlabel, NewLabelAdmin)
