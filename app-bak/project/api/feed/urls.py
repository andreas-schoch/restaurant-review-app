from django.urls import path
from .views import FeedDisplayView, UserFeedDisplay, FriendsFeedDisplay, FollowersFeedDisplay

app_name = 'feed'

urlpatterns = [
    path('', FeedDisplayView.as_view(), name='feed_display'),
    path('<int:pk>/', UserFeedDisplay.as_view(), name='user_feed_display'),
    path('followers/', FollowersFeedDisplay.as_view(), name='followers_feed_display'),
    path('friends/', FriendsFeedDisplay.as_view(), name='friends_feed_display'),
]
