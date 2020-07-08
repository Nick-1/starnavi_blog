# from django.db.models import Count
# from django.db.models.functions import TruncDay
# from rest_framework import generics
# from datetime import datetime
# import pytz
# from analytics.serializers import LikeListSerializer
# from posts.models import Like
#
#
# class LikeListView(generics.ListAPIView):
#     serializer_class = LikeListSerializer
#     queryset = Like.objects.all()
#
#     def get_queryset(self):
#         queryset = Like.objects.all()
#         date_from = self.request.query_params.get('date_from', None)
#         date_to = self.request.query_params.get('date_to', None)
#         if date_from and date_to is not None:
#             date_from = datetime.strptime(date_to, '%Y-%m-%d')
#             date_to = datetime.strptime(date_to, '%Y-%m-%d')
#             queryset = queryset.filter(created__range=[
#                 datetime(date_from, tzinfo=pytz.UTC),
#                 datetime(date_to, tzinfo=pytz.UTC)]).annotate(day=TruncDay('created')).values('day').annotate(count=Count('id')).values('day', 'count')
#         return queryset