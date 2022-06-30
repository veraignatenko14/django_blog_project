from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'published']
    list_filter = ['created_at', 'published']


admin.site.register(Post, PostAdmin)
