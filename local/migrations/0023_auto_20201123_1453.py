# Generated by Django 3.0.8 on 2020-11-23 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('local', '0022_auto_20201123_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newlabel',
            name='label_home',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]