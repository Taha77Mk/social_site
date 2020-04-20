from django.contrib import admin
from .models import Post, comments
admin.site.register(Post)
admin.site.register(comments)
