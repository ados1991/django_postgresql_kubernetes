from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class get_delete_update_post(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"


class get_post_posts(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ('userId',)

