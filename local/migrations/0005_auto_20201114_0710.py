# Generated by Django 3.0.8 on 2020-11-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0004_remove_userslist_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userslist',
            name='last_name',
            field=models.CharField(default=0, max_length=32),
        ),
        migrations.AddField(
            model_name='userslist',
            name='pass_code',
            field=models.CharField(default=0, max_length=64),
        ),
    ]
