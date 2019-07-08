from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.feed.models import Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'created', 'user']
        read_only_fields = ['id', 'created', 'user']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            **data,
            'like_count': instance.likes.count(),
        }

    def create(self, validated_data):
        return Post.objects.create(
            **validated_data,
            user=self.context.get('request').user,
        )
