from django.db.models import Count
from django.db.models.functions import TruncDay
from django.shortcuts import render
from rest_framework import generics

from analytics.serializer import LikeListSerializer
from posts.models import Like


class LikeListView(generics.ListAPIView):
    serializer_class = LikeListSerializer

    def get_queryset(self):
        queryset = Like.objects.all()
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        if date_from and date_to is not None:
            queryset = queryset.filter(created__range=[date_from, date_to]).annotate(day=TruncDay('created')).values('day').annotate(count=Count('id')).values('day', 'count')
        return queryset
