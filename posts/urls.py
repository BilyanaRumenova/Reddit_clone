from django.urls import path

from reddit_clone.posts.views import PostList, VoteCreate, PostRetrieveUpdateDestroy

urlpatterns = (
    path('', PostList.as_view()),
    path('<int:pk>/vote', VoteCreate.as_view()),
    path('<int:pk>', PostRetrieveUpdateDestroy.as_view()),
)