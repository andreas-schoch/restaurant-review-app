from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class MeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False,
        allow_blank=False,
    )

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
            raise serializers.ValidationError('Username is already taken!')
        except User.DoesNotExist:
            return username

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']
