from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('reddit_clone.posts.urls')),
    path('auth/', include('rest_framework.urls')),
]
