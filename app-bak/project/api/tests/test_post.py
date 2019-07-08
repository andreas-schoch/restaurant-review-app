from django.contrib.auth import get_user_model
from rest_framework import status

from project.api.tests.master_tests import MasterTestWrapper
from project.feed.models import Post, Like

User = get_user_model()


class GetUpdateDeletePostTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:post:post_detail'
    methods = ['GET', 'POST', 'DELETE']

    def get_kwargs(self):
        return {
            'pk': self.post.id
        }

    def setUp(self):
        super().setUp()
        self.post = Post.objects.create(
            user=self.user,
            content=f'Test post!',
        )
        self.url = self.get_url(**self.kwargs)

    def test_get_post(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('content'), 'Test post!')

    def test_update_post(self):
        self.authorize()
        response = self.client.post(self.url, {'content': 'New content!'})
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Post.objects.get(pk=self.post.id).content, 'New content!')

    def test_update_not_owner_post(self):
        self.authorize(self.other_user)
        response = self.client.post(self.url, {'content': 'New content!'})
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(Post.objects.get(pk=self.post.id).content, 'Test post!')

    def test_delete_post(self):
        self.authorize()
        response = self.client.delete(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Post.objects.filter(pk=self.post.id).count(), 0)

    def test_delete_not_owner_post(self):
        self.authorize(self.other_user)
        response = self.client.post(self.url, {'content': 'New content!'})
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIsNotNone(Post.objects.get(pk=self.post.id))


class CreatePostTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:post:post_create'
    methods = ['POST']

    def setUp(self):
        super().setUp()
        self.url = self.get_url(**self.kwargs)

    def test_create_post(self):
        self.authorize()
        response = self.client.post(self.url, {'content': 'Test post!'})
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('content'), 'Test post!')
        self.assertEquals(Post.objects.first().content, 'Test post!')


class ListLikedPostTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:post:list_liked_posts'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        for i in range(3):
            post = Post.objects.create(
                user=self.other_user,
                content=f'Test content! {i}'
            )
            Like.objects.create(
                user=self.user,
                post=post
            )

        self.url = self.get_url(**self.kwargs)

    def test_list_liked_posts(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 3)


class LikeDislikePostTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:post:like_dislike_post'
    methods = ['POST', 'DELETE']

    def get_kwargs(self):
        return {
            'pk': self.post.id
        }

    def setUp(self):
        super().setUp()
        self.post = Post.objects.create(
            user=self.other_user,
            content=f'Test content!'
        )
        self.url = self.get_url(**self.kwargs)

    def test_like_post(self):
        self.authorize()
        response = self.client.post(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Like.objects.filter(post=self.post, user=self.user).count(), 1)

    def test_remove_like_post(self):
        Like.objects.create(
            user=self.user,
            post=self.post
        )
        self.authorize()
        response = self.client.delete(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Like.objects.filter(post=self.post, user=self.user).count(), 0)


class SharePostTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:post:share_post'
    methods = ['POST']

    def get_kwargs(self):
        return {
            'pk': self.post.id
        }

    def setUp(self):
        super().setUp()
        self.post = Post.objects.create(
            user=self.other_user,
            content=f'Test content!'
        )
        self.url = self.get_url(**self.kwargs)

    def test_share_post(self):
        self.authorize()
        response = self.client.post(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Post.objects.filter(user=self.user, shared=self.post).count(), 1)
