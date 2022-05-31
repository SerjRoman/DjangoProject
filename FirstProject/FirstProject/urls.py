from django.contrib import admin
from django.urls import path
from FirstApp.views import index, father 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', father),
    path('index/', index, name='index'), 
]
