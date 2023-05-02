from django.contrib import admin
from .models import Post
from auth.models import UserProfile

admin.site.register(Post)
admin.site.register(UserProfile)
