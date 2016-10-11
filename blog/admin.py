from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content']
    search_fields = ['content']


class CommentAdmin(admin.ModelAdmin):
    field = ['author', 'text']
    search_fields = ['text']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
