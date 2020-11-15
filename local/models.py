from django.db import models

# # Create your models here.
class Userslist(models.Model):
    # Userslist with this Email name already exists.
    email_name = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64, default=None)
    last_name = models.CharField(max_length=64, default=None)
    pass_code = models.CharField(max_length=256, default=None)


class Newlabel(models.Model):
    label_name = models.CharField(max_length=64)

class Newitem(models.Model):
    item_name = models.CharField(max_length=64)
    item_price = models.PositiveIntegerField(default = 0)
    item_label = models.CharField(max_length=64)
