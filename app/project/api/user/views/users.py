from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..serializers import UserSerializer

User = get_user_model()


class UsersListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def filter_queryset(self, queryset):
        search_string = self.request.query_params.get('search')
        if search_string:
            queryset = queryset.filter(
                Q(username__contains=search_string) |
                Q(email__contains=search_string) |
                Q(first_name__contains=search_string) |
                Q(laster_name__contains=search_string)
            )
        return queryset


class UserGetView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
