from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Newlabel(models.Model):
    label_home = models.CharField(max_length=64, null=True)
    label_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.label_name}"

class Newitem(models.Model):
    Veg_choices = [('Veg', 'Veg'),
                   ('Non-Veg', 'Non-Veg')]
    item_name = models.CharField(max_length=64, unique=True)
    item_label = models.ForeignKey(Newlabel, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=30,choices=Veg_choices,null=True)
    item_price = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.item_name}"
