from django.contrib import admin
from .models import Category, News

class NewsModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author","category"]
    list_display_links = ["author"]
    list_filter = ["category","created"]
    search_fields = ["title","intro","content"]

# Register your models here.

admin.site.register(Category)
admin.site.register(News, NewsModelAdmin)
