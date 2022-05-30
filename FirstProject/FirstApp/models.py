from django.db import models

# Create your models here.
class Book(models.Model):
    NAME = models.CharField(max_length=255,blank=True, null=True)
    AUTHOR = models.CharField(max_length=255,blank=True, null=True)
    RAITING = models.CharField(max_length=255,blank=True, null=True)
    DESCRIPTION = models.CharField(max_length=255,blank=True, null=True) # blank = True - данное поле может быть пустым
    PRICE = models.CharField(max_length=255,blank=True, null=True)
    IMAGE = models.CharField(max_length=255,blank=True, null=True)
    DATE = models.CharField(max_length=255,blank=True, null=True)
    COUNT_RAITING = models.CharField(max_length=255,blank=True, null=True)