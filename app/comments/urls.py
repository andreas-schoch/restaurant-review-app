from django.urls import path
from .views import (CommentCreateAPIView,)


urlpatterns = [
    # path('review/comment/<int:pk>/', UserComments.as_view(), name='user-search'),
    path('restaurant/comment/new/<int:pk>/', CommentCreateAPIView.as_view(), name='user-search'),
    # path('review/comment/delete/<int:pk>/', DeleteReviewsComments.as_view(), name='user-search'),
    # path('review/comment/like/<int:pk>/', LikeOrUnLikeComment.as_view(), name='user-search'),

]
