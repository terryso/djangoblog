from django.contrib import admin
from django.contrib.admin import ModelAdmin

from blog.models import Post

admin.site.register(Post, ModelAdmin)
