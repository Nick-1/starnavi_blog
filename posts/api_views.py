from django.core.exceptions import ObjectDoesNotExist
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

        try:
            like = Like.objects.get(post_id=kwargs['pk'])
            if request.user.id == like.user_id:
                like.delete()
            else:
                return Response(status=status.HTTP_403_FORBIDDEN,
                                data={'message': 'You do not have permission to perform this action.'})
        except (ObjectDoesNotExist, ValueError):
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'object was not found'})
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'object was successfully deleted'})
