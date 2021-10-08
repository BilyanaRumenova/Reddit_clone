from django.contrib import admin

from reddit_clone.posts.models import Post, Vote

admin.site.register(Post)

admin.site.register(Vote)