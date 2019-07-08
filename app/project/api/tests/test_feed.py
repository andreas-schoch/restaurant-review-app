from django.contrib.auth import get_user_model
from rest_framework import status

from project.api.tests.master_tests import MasterTestWrapper
from project.feed.models import Post, FriendRequest

User = get_user_model()


class FeedDisplayTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:feed:feed_display'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        for i in range(10):
            Post.objects.create(
                user=self.user,
                content=f'Test post! {i}',
            )
        self.url = self.get_url(**self.kwargs)

    def test_post_feed_lenght(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 10)

    def test_post_feed_sort_descending_check(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data[0].get('content'), 'Test post! 9')


class UserFeedDisplayTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:feed:user_feed_display'
    methods = ['GET']

    def get_kwargs(self):
        return {
            'pk': self.user.id
        }

    def setUp(self):
        super().setUp()
        for i in range(10):
            Post.objects.create(
                user=self.user,
                content=f'Test post! {i}',
            )
            Post.objects.create(
                user=self.other_user,
                content=f'Test post! {i}',
            )
        self.url = self.get_url(**self.kwargs)

    def test_post_feed_lenght(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 10)

    def test_post_feed_sort_descending_check(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data[0].get('content'), 'Test post! 9')


class FollowersFeedDisplayTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:feed:followers_feed_display'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        self.user.user_profile.followees.add(self.other_user)
        for i in range(10):
            Post.objects.create(
                user=self.user,
                content=f'Test post! {i}',
            )
            Post.objects.create(
                user=self.other_user,
                content=f'Test post! {i}',
            )
        self.url = self.get_url(**self.kwargs)

    def test_post_feed_lenght(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 10)

    def test_post_owner(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data[0].get('user'), self.other_user.id)


class FriendsFeedDisplayTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:feed:friends_feed_display'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        FriendRequest.objects.create(
            requester=self.user,
            receiver=self.other_user,
            status='accepted',
        )
        for i in range(10):
            Post.objects.create(
                user=self.user,
                content=f'Test post! {i}',
            )
            Post.objects.create(
                user=self.other_user,
                content=f'Test post! {i}',
            )
        self.url = self.get_url(**self.kwargs)

    def test_post_feed_lenght(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 10)

    def test_post_owner(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data[0].get('user'), self.other_user.id)
