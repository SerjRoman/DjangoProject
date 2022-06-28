from unicodedata import category
from django.contrib import admin
# from django.contrib import mark_safe
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Rewiews 
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)

class ShowRewiws(admin.TabularInline):#StackedInline, TabularInline
    model = Rewiews
    extra = 1#one empty fiel, dmore fields for rewiew
    readonly_fields = ("name", "email")

class ShowMovieShots(admin.StackedInline):
    movie = MovieShots
    extra = 1

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    
    list_display = ("id", "title", "category", "url", "draft")
    list_filter = ("category", "year")
    list_display_links = ("title",)
    search_fields = ("title", "category__name")
    inlines = [ShowRewiws, ]#ShowMovieShots
    save_on_top= True
    list_editable = ("draft",)
    # fields = (("actors", "deirectors", "genres"),)
    fieldsets = (
        (None, {#1None can be a name of group 
            #2 u can also write for using function hide and show
            #"classes":("collapse",),
            "fields": ("title",)
        }),
        (None, {
            "fields": ("poster", "description",)
        }),
        (None, {
            "fields": (("country","world_premiere", "year"),)
        }),
        (None, {
            "fields": (("actors", "directors"), ("category", "genres"),)
        }),
        (None, { 
            "fields": (("budget", "fees_in_world"),)
        }),
        (None, {
            "fields": ("url", "draft",)
        }),
    )

@admin.register(Rewiews)
class RewiewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name","email", "parent", "movie")
    readonly_fields = ("name", "email")

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "image")
    

    # def get_image(self, obj):
    #     return (f'<img scr={obj.image.url} width="50" height="60')
    # get_image.short_description = "Imag32132e"

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "movie", "ip")



admin.site.register(RatingStar)
admin.site.register(MovieShots)

admin.site.site_title = "???"
admin.site.site_header = "???"