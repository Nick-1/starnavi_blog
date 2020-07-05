from django.shortcuts import render
from rest_framework import generics

from posts.models import Post
from posts.serializers import PostListSerializer, PostDetailSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
