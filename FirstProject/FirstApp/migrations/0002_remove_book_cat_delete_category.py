# Generated by Django 4.0.4 on 2022-06-19 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='CAT',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]