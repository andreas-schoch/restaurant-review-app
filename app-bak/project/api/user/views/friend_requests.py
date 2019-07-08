from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from project.feed.models import FriendRequest
from ..serializers import FriendRequestSerializer, UserSerializer
from ..permissions import IsFRReceiverOrReadOnly

User = get_user_model()


class FriendRequestsListView(ListAPIView):
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()

    def filter_queryset(self, queryset):
        queryset = queryset.filter(
            Q(status='pending'),
            Q(receiver=self.request.user)
        )
        return queryset


class SendFriendRequestView(GenericAPIView):
    serializer_class = FriendRequestSerializer
    queryset = User.objects.all()

    def post(self, request, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer()
        f_request = serializer.save(
            requester=request.user,
            receiver=user,
        )
        return Response(FriendRequestSerializer(f_request).data)


class PendingFriendRequestListView(ListAPIView):
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()

    def filter_queryset(self, queryset):
        queryset = queryset.filter(
            Q(status='pending'),
            Q(requester=self.request.user)
        )
        return queryset


class AcceptFriendRequestView(GenericAPIView):
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsFRReceiverOrReadOnly,
    ]

    def post(self, request, *args, **kwargs):
        friend_request = self.get_object()
        friend_request.status = 'accepted'
        friend_request.save()
        return Response(self.get_serializer(friend_request).data)


class RejectFriendRequestView(GenericAPIView):
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsFRReceiverOrReadOnly,
    ]

    def post(self, request, *args, **kwargs):
        friend_request = self.get_object()
        friend_request.status = 'rejected'
        friend_request.save()
        return Response(self.get_serializer(friend_request).data)


class FriendsListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def filter_queryset(self, queryset):
        queryset = queryset.filter(
            Q(connections__status='accepted') |
            Q(friend_requests__status='accepted'),
            Q(connections__requester=self.request.user) |
            Q(connections__receiver=self.request.user) |
            Q(friend_requests__requester=self.request.user) |
            Q(friend_requests__receiver=self.request.user)
        ).exclude(id=self.request.user.id).distinct()
        return queryset
