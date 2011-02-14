from chatofido.blog.models import Post, Blog, Image, Comment
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified')
    list_filter = ['modified']
    search_fields = ['name']

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {'fields': ['author', 'title']}),
        ('Content'          , {'fields': ['content'], 'classes': ['collapse']}),
        ]
    list_display = ('title', 'author', 'created')
    list_filter = ['created']
    search_fields = ['title', 'author']


class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {'fields': ['author', 'title']}),
        ('Content'          , {'fields': ['content', 'image'], 'classes': ['collapse']}),
        ]

class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {'fields': ['author']}),
        ('Content'          , {'fields': ['content'], 'classes': ['collapse']})
        ]
    list_display = ('author', 'created', 'content')
    list_filter = ('author', 'created')
    
admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, CommentAdmin)
