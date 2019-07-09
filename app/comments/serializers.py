from rest_framework import serializers
from api.models import Comment


class CommentsSerializer(serializers.ModelSerializer):



    class Meta:
        model = Comment
        fields = ['author', 'restaurant', 'body', 'image', 'rating', 'created', 'modified']
        read_only_fields = ['id', 'created', 'modified']
