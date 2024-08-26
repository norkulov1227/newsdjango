from django.contrib import admin
from news.models import Category, News, Contact

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', )
    list_filter = ('created_at', )
    prepopulated_fields = {'slug': ('name',), }


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'description', 'body')
    list_filter = ('category', 'created_at')
    prepopulated_fields = {'slug': ('title', ), }

@admin.register(Contact)
class ContactAdmmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', )
    search_fields = ('full_name', 'email', 'subject', 'message')
    list_filter = ('created_at', )
