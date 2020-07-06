from rest_framework import generics
from posts.models import Post
from posts.serializers import PostListSerializer, PostDetailSerializer, LikeSerializer
from posts.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser, )


class LikeView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated, )

