from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers
from .models import Like
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, )


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LikeSerializer
    queryset = models.Like.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, )

    def destroy(self, request, *args, **kwargs):
        try:
            Like.objects.get(post_id=kwargs['pk']).delete()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'object was not found'})
        return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'object was successfully deleted'})