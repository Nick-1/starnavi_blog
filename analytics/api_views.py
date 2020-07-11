from django.db.models import Count
from django.db.models.functions import TruncDay
from rest_framework.permissions import IsAuthenticated

from analytics.serializers import LikeListSerializer
from posts.models import Like
from rest_framework import viewsets
from blog.settings import TIME_ZONE
import pytz
tz = pytz.timezone(TIME_ZONE)


class LikesCountViewSet(viewsets.ModelViewSet):
    serializer_class = LikeListSerializer
    queryset = Like.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Like.objects.all()
        q_from = self.request.query_params.get('date_from', None)
        q_to = self.request.query_params.get('date_to', None)
        user = self.request.user
        if q_from and q_to is not None:
            queryset = queryset.filter(user_id=user.id, created__range=[q_from, q_to])\
                .annotate(day=TruncDay('created')).values('day')\
                .annotate(count=Count('id')).values('day', 'count')
        return queryset
