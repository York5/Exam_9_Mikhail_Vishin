from django.urls import path, include
from rest_framework import routers

from api_v1.views import CommentViewSet, LikeViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
]
