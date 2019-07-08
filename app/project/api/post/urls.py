from django.urls import path
from .views import PostGetUpdateDeleteView, ListLikedPostsView, PostCreateView, LikeDislikePostView, SharePostView

app_name = 'post'

urlpatterns = [
    path('<int:pk>/', PostGetUpdateDeleteView.as_view(), name='post_detail'),
    path('new-post/', PostCreateView.as_view(), name='post_create'),
    path('likes/', ListLikedPostsView.as_view(), name='list_liked_posts'),
    path('like/<int:pk>/', LikeDislikePostView.as_view(), name='like_dislike_post'),
    path('share-post/<int:pk>/', SharePostView.as_view(), name='share_post'),
]
