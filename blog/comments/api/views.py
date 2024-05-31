from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from comments.models import Comment
from comments.api.serializers import CommnetSerializer
from django_filters.rest_framework import DjangoFilterBackend
from comments.api.permissions import IsOwnerOrReadAndCreateOnly
class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommnetSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter,DjangoFilterBackend]
    ordering = ['-create_at']
    filterset_fields = ['post']
