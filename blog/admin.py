from django.contrib import admin
from blog.models import Post, Usercomment

admin.site.register((Post, Usercomment))
