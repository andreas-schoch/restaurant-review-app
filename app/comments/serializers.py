from rest_framework import serializers
from api.models import Comment

class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id', 'created', 'modified']
