from unicodedata import category
from django.contrib import admin
from django.urls import path
from FirstApp.views import index, books, categories, tops, product_info


product = "Ubrilded Cowboy"

product_link = (product.replace(' ', '_')+ "/").lower() 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='main'),
    path('tops/', tops, name='tops'), 
    path('all/', categories, name='categories'),
    path('tops/books/', books, name='books'),
    path(product_link, product_info, name='info'),
    path('tops/book/', product_info, name='book'),
    path('tops/book/<int:book_id>', product_info, name='book'),
    
]
