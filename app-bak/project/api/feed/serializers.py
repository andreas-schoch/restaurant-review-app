from django.contrib.auth import get_user_model

from project.api.post.serializers import PostSerializer
from project.api.user.serializers import UserSerializer
from project.feed.models import Post

User = get_user_model()


class FeedDisplaySerializer(PostSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'content', 'created', 'user']
        read_only_fields = ['id', 'created', 'user']
