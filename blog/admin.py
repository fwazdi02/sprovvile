from django.contrib import admin

from .models import Category, Post, Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','icon', 'description', 'is_active')
    prepopulated_fields = {'slug': ('name',)}        
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category','image', 'content', 'user', 'last_update', 'status')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','body','name', 'email', 'created_date', 'status')
admin.site.register(Comment, CommentAdmin)
