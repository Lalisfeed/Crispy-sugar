# Generated by Django 3.0.8 on 2020-11-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0015_auto_20201123_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newitem',
            name='item_price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
