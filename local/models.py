from django.db import models

# # Create your models here.
class Userslist(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_name = models.EmailField()

class Newlabel(models.Model):
    label_name = models.CharField(max_length=64)

class Newitem(models.Model):
    item_name = models.CharField(max_length=64)
    item_price = models.PositiveIntegerField(default = 0)
    item_label = models.CharField(max_length=64)
