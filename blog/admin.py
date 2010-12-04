from chatofido.blog.models import Post, Blog
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified')
    list_filter = ['modified']
    search_fields = ['name']

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal information', {'fields': ['author', 'title']}),
        ('Content'             , {'fields': ['content'], 'classes': ['collapse']}),
        ]
    list_display = ('title', 'author', 'created')
    list_filter = ['created']
    search_fields = ['title', 'author']

    

admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)
