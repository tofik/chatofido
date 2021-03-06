from chatofido.blog.models import Post, Blog, Image, Comment
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified')
    list_filter = ['modified']
    search_fields = ['name']

class CommentsInLine(admin.TabularInline):
    model = Comment
    extra = 3

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {'fields': ['author', 'title']}),
        ('Content'          , {'fields': ['content', 'blog'], 'classes': ['collapse']}),
        ]
    list_display = ('title', 'author', 'created', 'blog')
    list_filter = ['created', 'blog']
    search_fields = ['title', 'author']
    inlines = [CommentsInLine]

class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {'fields': ['author', 'title']}),
        ('Content'          , {'fields': ['content', 'image', 'blog'], 'classes': ['collapse']}),
        ]

class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {'fields': ['author']}),
        ('Content'          , {'fields': ['content', 'post'], 'classes': ['collapse']})
        ]

    def get_blog(self):
        return Blog.objects.get(post=self.post)
    get_blog.short_description = "Blog"

    list_filter = ('author', 'created', 'post')
    list_display = ('author', 'created', 'content', 'post', get_blog)

    
     
admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, CommentAdmin)
