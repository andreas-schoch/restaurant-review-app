from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from rest_framework import serializers

from project.feed.models import FriendRequest

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()
    fame_index = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'post_count', 'fame_index']
        read_only_fields = fields

    def get_post_count(self, user):
        return user.posts.count()

    def get_fame_index(self, user):
        return sum([p.likes.count() for p in user.posts.all()])


class FriendRequestSerializer(serializers.ModelSerializer):
    requester = UserSerializer(
        read_only=True,
    )
    receiver = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = FriendRequest
        fields = ['requester', 'receiver', 'status']
        read_only_fields = fields

    @staticmethod
    def send_notification(**kwargs):
        requester = kwargs.get('requester')
        receiver = kwargs.get('receiver')
        message = EmailMessage(
            subject='Social feed friend request was sent to you',
            body=f'The user {requester.username} has sent you a friend request!',
            to=[receiver.email],
        )
        message.send()

    def save(self, **kwargs):
        f_request = FriendRequest.objects.create(**kwargs)
        self.send_notification(**kwargs)
        return f_request
