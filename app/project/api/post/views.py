from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from project.api.base import GetObjectMixin
from project.api.permissions import IsOwnerOrReadOnly
from project.feed.models import Post, Like
from .serializers import PostSerializer


class PostGetUpdateDeleteView(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

    def get(self, request, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, **kwargs):
        post = self.get_object()
        post.delete()
        return Response('OK')


class PostCreateView(GenericAPIView):
    serializer_class = PostSerializer

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        post = serializer.create(serializer.validated_data)
        return Response(PostSerializer(post).data)


class ListLikedPostsView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(likes__user=self.request.user)


class ListUserPostsView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(user__username=self.request.user.username)


class LikeDislikePostView(GetObjectMixin, GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def post(self, request, **kwargs):
        post = self.get_object()
        Like.objects.get_or_create(
            user=request.user,
            post=post
        )
        return Response('Post liked!')

    def delete(self, request, **kwargs):
        post = self.get_object()
        like = self.get_object_by_model(Like, post=post, user=request.user)
        like.delete()
        return Response('Like removed!')


class SharePostView(GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def post(self, request, **kwargs):
        post = self.get_object()
        post = Post.objects.create(
            shared=post,
            user=request.user,
        )
        return Response(PostSerializer(post).data)
