"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from blog.views import StartPageView
from user_app.views import LoginView, RegistrationUserView, UserActionsView
from rest_framework import routers
from posts import api_views as posts_views
from analytics import api_views as analytics_views
from constants import API_URL, USER_LOGIN_URL, USER_REGISTRATION_URL, USER_URL, \
    POST_ROUT, LIKE_ROUT, LIKES_COUNT_ROUT, ACTIONS_URL

router = routers.DefaultRouter()
router.register(rf'{POST_ROUT}', posts_views.PostViewSet)
router.register(rf'{LIKE_ROUT}', posts_views.LikeViewSet)
router.register(rf'{LIKES_COUNT_ROUT}', analytics_views.LikesCountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StartPageView.as_view()),
    path(API_URL, include(router.urls)),

    path(USER_LOGIN_URL, LoginView.as_view(), name='jwt-login'),
    path(f'{USER_LOGIN_URL}refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),

    path(USER_REGISTRATION_URL, RegistrationUserView.as_view(), name='registration'),
    path(f'{USER_URL}<int:pk>/{ACTIONS_URL}/', UserActionsView.as_view(), name='actions')
]
