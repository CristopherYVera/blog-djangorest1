from rest_framework.routers import DefaultRouter
from comments.api.views import CommentApiViewSet

router_commnets = DefaultRouter()
router_commnets.register(prefix='comments',basename='comments',viewset=CommentApiViewSet)