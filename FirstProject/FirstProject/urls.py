from django.contrib import admin
from django.urls import path
from FirstApp.views import index, father 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', father, name='main'),
    path('index/', index, name='index'), 
]
