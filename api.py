from rest_framework import routers
from posts import api_views as posts_views
from analytics import api_views as analytics_views

router = routers.DefaultRouter()
router.register(r'posts', posts_views.PostViewSet)
router.register(r'like', posts_views.LikeViewSet)
router.register(r'likescount', analytics_views.LikesCountViewSet)
