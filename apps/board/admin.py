from django.contrib import admin
from .models import Post,Board,Comment
# Register your models here.
admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Comment)
