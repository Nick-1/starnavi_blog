from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers
from .models import Like
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, )
    queryset = models.Post.objects.filter(draft=False)


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LikeSerializer
    queryset = models.Like.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def destroy(self, request, *args, **kwargs):
        Like.objects.filter(user=request.user, post_id=kwargs['pk']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'object was successfully deleted'})
