from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post
from .serializer import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
