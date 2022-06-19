from unicodedata import category
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from FirstApp.views import index, books, categories, tops, post_info


product = "Ubrilded Cowboy"

product_link = (product.replace(' ', '_')+ "/").lower() 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='main'),
    path('tops/', tops, name='tops'), 
    path('all/', categories, name='categories'),
    path('tops/books/', books, name='books'),
    path('tops/book/<int:book_id>', post_info, name='book'),
    path('tops/', include("movies.urls")),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)