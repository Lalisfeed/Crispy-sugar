from django.db import models

# # Create your models here.
class Newlabel(models.Model):
    label_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.label_name}"

class Newitem(models.Model):
    item_name = models.CharField(max_length=64)
    item_label = models.ForeignKey(Newlabel, on_delete=models.CASCADE)
