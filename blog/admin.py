from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'is_published', 'created_at', 'updated_at')
    search_fields = ('title', 'body')
    list_filter = ('is_published', 'created_at')
    ordering = ('-created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'is_approved', 'created_at')
    search_fields = ('body',)
    list_filter = ('is_approved', 'created_at')
    ordering = ('-created_at',)