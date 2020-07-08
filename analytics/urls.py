from django.urls import path
from analytics.views import LikeListView

urlpatterns = [
    path('likescount/', LikeListView.as_view()),
]