from django.urls import path
from .views import (CommentListCreateAPIView,
                    )


urlpatterns = [
    path('', CommentListCreateAPIView.as_view(), name='restaurant-comment'),
    # path('review/comment/delete/<int:pk>/', DeleteReviewsComments.as_view(), name='user-search'),
    # path('review/comment/like/<int:pk>/', LikeOrUnLikeComment.as_view(), name='user-search'),

]
