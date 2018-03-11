from django.contrib import admin
from .models import Post,Board,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('board','title', 'author')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','author')
admin.site.register(Board)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
