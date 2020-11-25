from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Newlabel(models.Model):
    label_home = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    label_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.label_name}"


class Newitem(models.Model):
    item_womb = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=64, unique=True)
    item_label = models.CharField(max_length=64,null=True)
    item_type = models.CharField(max_length=30,null=True)
    item_price = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.item_name}"

    # Veg_choices = [('Veg', 'Veg'),
    #                ('Non-Veg', 'Non-Veg')]

class Neworder(models.Model):
    item_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item_order_label = models.CharField(max_length=64, null=True)
    item_order_name = models.CharField(max_length=64, unique=True)
    item_order_number = models.PositiveIntegerField(null=True)
    item_order_price = models.PositiveIntegerField(null=True)
    item_order_total_price = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.item_order_total_price}"