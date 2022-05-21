from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    raiting = models.CharField(max_length=255)
    description = models.TextField(blank= True) # blank = True - данное поле может быть пустым
    price = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)