from django.db import models

# Create your models here.
class Book(models.Model):
    NAME = models.CharField(max_length=255,blank=True, null=True)
    AUTHOR = models.CharField(max_length=255,blank=True, null=True)
    RAITING = models.CharField(max_length=255,blank=True, null=True)
    PRICE = models.CharField(max_length=255,blank=True, null=True)
    IMAGE = models.CharField(max_length=255,blank=True, null=True)
    DESCRIPTION_SHORT = models.TextField(blank=True, null=True) # blank = True - данное поле может быть пустым
    DESCRIPTION = models.TextField(blank=True, null=True) # blank = True - данное поле может быть пустым
    DATE = models.CharField(max_length=255,blank=True, null=True)
    COUNT_RAITING = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        
        return f'{self.NAME}'