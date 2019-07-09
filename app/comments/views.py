from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from api.models import Comment
from .serializers import CommentsSerializer
from rest_framework.generics import get_object_or_404


class CommentListCreateAPIView(generics.ListCreateAPIView):
    """
    Class to GET all Comments or POST a Comment for a restaurant
    """
    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status 201": "Comment created succesfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDeleteUpdateRestaurant(generics.RetrieveUpdateDestroyAPIView):
    """
    Class to GET - PUT/PATCH (UPDATE) - DELETE: Comment by id
    """
    serializer_class = CommentsSerializer

    def get_object(self, pk):
        post = get_object_or_404(Comment, pk=pk)
        return post

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = CommentsSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = CommentsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status 201": "Comment updated succesfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response({"Status 204": "Comment deleted succesfully"}, status=status.HTTP_204_NO_CONTENT)
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
