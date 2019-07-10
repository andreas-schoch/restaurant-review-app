from rest_framework import serializers
from api.models import Comment, Reaction


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'author', 'restaurant', 'body', 'image', 'rating', 'created', 'modified']
        read_only_fields = ['id', 'created', 'modified']


class ReactionLightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reaction
        fields = ['id', 'comment']
        read_only_fields = ['id']


class ReactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reaction
        fields = ['id', 'user_reacted', 'comment']
        read_only_fields = ['id']