from django.db import models


# Create your models here.
class Log_in(models.Model):
    user_name = models.CharField('Name', max_length = 200)
    user_surname = models.CharField('Surname', max_length = 200)
    user_email = models.CharField('Email', max_length = 200)
    password = models.CharField('Password', max_length = 200)
    