from django.contrib import admin
from .models import Post, Comment, Tag


class PostAdmin(admin.ModelAdmin):
    exclude = ['author']
    search_fields = ['content']


class CommentAdmin(admin.ModelAdmin):
    exclude = []
    search_fields = ['text']


class TagAdmin(admin.ModelAdmin):
    exclude = []

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
