# Generated by Django 3.0.8 on 2020-11-23 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0016_auto_20201123_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]