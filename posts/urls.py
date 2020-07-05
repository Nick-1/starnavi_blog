from django.urls import path

from posts.views import PostListView, PostCreateView, PostDetailView, LikeUnlikeView

urlpatterns = [
    path('all/', PostListView.as_view()),
    path('post/create/', PostCreateView.as_view()),
    path('post/detail/<int:pk>/', PostDetailView.as_view()),
    path('post/likeunlike/', LikeUnlikeView.as_view()),
]