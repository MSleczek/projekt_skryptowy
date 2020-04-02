from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'slug', 'status','dodano')
    list_filter = ("status",)
    search_fields = ['tytul', 'tresc']
    prepopulated_fields = {'slug': ('tytul',)}
  
admin.site.register(Post, PostAdmin)
