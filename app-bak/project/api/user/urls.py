from django.urls import path
from .views.followers import FollowUnfollowUserView, FollowersListView, FollowingListView
from .views.users import UsersListView, UserGetView
from .views import friend_requests

app_name = 'user'

urlpatterns = [
    path('', UsersListView.as_view(), name='users_list'),
    path('<int:pk>/', UserGetView.as_view(), name='user_get'),
    path('followers/', FollowersListView.as_view(), name='followers_list'),
    path(
        'following/',
        FollowingListView.as_view(),
        name='following_list'
    ),
    path(
        'follow/<int:pk>/',
        FollowUnfollowUserView.as_view(),
        name='follow_unfollow_user'
    ),
    path(
        'friends/',
        friend_requests.FriendsListView.as_view(),
        name='friend_list'
    ),
    path(
        'friendrequests/',
        friend_requests.FriendRequestsListView.as_view(),
        name='friend_requests_list'
    ),
    path(
        'friendrequests/<int:pk>/',
        friend_requests.SendFriendRequestView.as_view(),
        name='send_friend_request'
    ),
    path(
        'friendrequests/pending/',
        friend_requests.PendingFriendRequestListView.as_view(),
        name='pending_friend_request_list'
    ),
    path(
        'friendrequests/accept/<int:pk>/',
        friend_requests.AcceptFriendRequestView.as_view(),
        name='accept_friend_request'
    ),
    path(
        'friendrequests/reject/<int:pk>/',
        friend_requests.RejectFriendRequestView.as_view(),
        name='reject_friend_request'
    ),
]
