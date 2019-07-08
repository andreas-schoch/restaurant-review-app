from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from project.api.base import GetObjectMixin
from project.feed.models import Post
from project.api.post.serializers import PostSerializer
from .serializers import FeedDisplaySerializer

User = get_user_model()


class FeedDisplayView(ListAPIView):
    serializer_class = FeedDisplaySerializer
    queryset = Post.objects.all()

    def filter_queryset(self, queryset):
        search_string = self.request.query_params.get('search')
        if search_string:
            queryset = queryset.filter(content__contains=search_string)
        return queryset


class UserFeedDisplay(GetObjectMixin, ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self, **kwargs):
        return self.queryset.filter(user=kwargs.get('user'))

    def list(self, request, *args, **kwargs):
        user = self.get_object_by_model(User, pk=kwargs.get('pk'))
        queryset = self.get_queryset(user=user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class FollowersFeedDisplay(GetObjectMixin, ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def filter_queryset(self, queryset):
        queryset = queryset.filter(user__followers=self.request.user.user_profile)
        return queryset


class FriendsFeedDisplay(GetObjectMixin, ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def filter_queryset(self, queryset):
        queryset = queryset.filter(
            Q(user__connections__status='accepted') |
            Q(user__friend_requests__status='accepted'),
            Q(user__connections__requester=self.request.user) |
            Q(user__connections__receiver=self.request.user) |
            Q(user__friend_requests__requester=self.request.user) |
            Q(user__friend_requests__receiver=self.request.user)
        ).exclude(user=self.request.user).distinct()
        return queryset
