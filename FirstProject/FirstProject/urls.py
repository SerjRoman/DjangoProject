from django.contrib import admin
from django.urls import path
from FirstApp.views import index
from Regform.views import regForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('reg/', regForm, name='reg'),
]
