# from api.permissions import IsOwnerOrReadOnly
# from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework import generics


from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404

User = get_user_model()

from api.models import (UserProfile,
                        Restaurant,
                        Reaction,
                        Comment,
                        Ownership)

from users.serializers import (UserSerializer,
                               UserProfileSerializer,
                               UserNestedSerializer,
                               )


class UserProfilesView(generics.ListAPIView):
    """
    Class to GET all User Profiles
    """
    queryset = User.objects.all()
    serializer_class = UserNestedSerializer
    #permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class GetUpdateUserProfileView(generics.RetrieveUpdateAPIView):
    """
    Class to GET and UPDATE the User's Profile
    """
    serializer_class = UserNestedSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        self.kwargs['pk'] = self.request.user.id  # the view expects a lookup field in the url e.g. api/me/<pk>

        return self.queryset


class UserProfileView(APIView):
    """
    Class to GET a User Profile using the user_id
    """
    @staticmethod
    def get_user_profile(pk):
        user_profile = get_object_or_404(User, pk=pk)
        return user_profile

    def get(self, request, pk):
        user_profile = self.get_user_profile(pk)
        serializer = UserNestedSerializer(user_profile)
        return Response(serializer.data)


class SearchUser(generics.ListAPIView):
    """
    Class to Search a User Profile
    """
    permission_classes = []
    authentication_classes = []

    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'last_name', 'first_name', 'email')



