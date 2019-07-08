from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from project.api.base import GetObjectMixin
from project.feed.models import UserProfile

from ..serializers import UserSerializer

User = get_user_model()


class FollowUnfollowUserView(GetObjectMixin, APIView):

    def post(self, request, pk):
        user = self.get_object_by_model(User, pk=pk)
        user_profile = request.user.user_profile
        user_profile.followees.add(user)
        return Response('OK')

    def delete(self, request, pk):
        user = self.get_object_by_model(User, pk=pk)
        my_user = request.user
        user_profile, created = UserProfile.objects.get_or_create(user=my_user)
        user_profile.followees.remove(user)
        return Response('OK')


class FollowersListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(user_profile__followees=self.request.user)


class FollowingListView(FollowersListView):
    def filter_queryset(self, queryset):
        return queryset.filter(followers=self.request.user.user_profile)
