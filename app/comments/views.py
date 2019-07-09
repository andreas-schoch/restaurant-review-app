# from rest_framework.generics import (ListAPIView,
#                                      CreateAPIView,
#                                      DestroyAPIView,
#                                      RetrieveUpdateDestroyAPIView)

# from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from api.models import Comment
from .serializers import CommentsSerializer


class CommentCreateAPIView(APIView):
    """
    Class to POST a Comment
    """

    def get(self, request):
        comment = Comment.objects.first()
        serializer = CommentsSerializer(comment)
        return Response({"This is a typical Json post": {"required": "title, body, author"}, "data": serializer.data})

    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status 201": "Post created succesfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# class UserComments(ListAPIView):
#     serializer_class = CommentsSerializer
#     queryset = Comment.objects.all()
#
#     def get_queryset(self):
#         return self.queryset.filter(comment_owner__id=self.kwargs.get('pk'))

#
# # making a new comment
# class CreateReviewsComments(CreateAPIView):
#     serializer_class = CommentsSerializer
#     queryset = Comments_on_reviews.objects.all()
#
#     def get_object(self):
#         try:
#             return Restaurant_review.objects.get(pk=self.kwargs.get('pk'))
#         except Restaurant_review.DoesNotExist:
#             raise NotFound('Review not found with id whatever')
#
#     def perform_create(self, serializer):
#         serializer.save(restaurant_review=self.get_object(), comment_owner=self.request.user)
#
#
# # delete a comment
# class DeleteReviewsComments(DestroyAPIView):
#     serializer_class = CommentsSerializer
#     queryset = Comments_on_reviews.objects.all()
#
#     def get_queryset(self):
#         return self.queryset.filter(id=self.kwargs.get('pk'))
#
#
# # Like and Remove a Like  from a review comment
# class LikeOrUnLikeComment(RetrieveUpdateDestroyAPIView):
#     serializer_class = CommentsSerializer
#     queryset = Comments_on_reviews.objects.all()
#
#     def post(self, request, pk, **kwargs):
#         self.get_object()
#         like, created = CommentLikes.objects.get_or_create(comment_like_owner=self.request.user)
#         return Response('Liked')
#
#     def delete(self, request, *args, **kwargs):
#         self.get_object()
#         try:
#             like, created = CommentLikes.objects.get(comment_like_owner=self.request.user).delete()
#         except CommentLikes.DoesNotExist:
#             return Response({'you cant Unlike twice'}, 400)
#         return Response('Unliked')
