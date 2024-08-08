from django.contrib import admin

# Register your models here.

from .models import Movie
from .models import Category
from .models import Comment



class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'created_at')
    list_display_links = ('id', 'title')

    list_editable = ('is_published',)
    search_fields = ('title', 'category')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)
admin.site.register(Comment)


