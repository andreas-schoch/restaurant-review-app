from django.core import mail
from django.contrib.auth import get_user_model
from rest_framework import status

from project.api.tests.master_tests import MasterTestWrapper
from project.feed.models import FriendRequest

User = get_user_model()


class ListUsersTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:user:users_list'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        self.users = []
        for i in range(3):
            self.users.append(
                User.objects.create_user(
                    username=f'user_{i}',
                    password=f'super_secure_{i}',
                )
            )
        self.url = self.get_url(**self.get_kwargs())

    def test_number_of_users(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), len(self.users) + 2)


class GetUserTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:user:user_get'
    methods = ['GET']

    def get_kwargs(self):
        return {
            'pk': self.user.id,
        }

    def setUp(self):
        super().setUp()
        self.url = self.get_url(**self.get_kwargs())

    def test_get_user(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('username'), self.user.username)


class FollowersListTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:user:followers_list'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        self.users = []
        for i in range(3):
            user = User.objects.create_user(
                username=f'user_{i}',
                password=f'super_secure_{i}',
            )
            user.user_profile.followees.add(self.user)
            self.users.append(user)
        self.url = self.get_url(**self.get_kwargs())

    def test_number_of_followers(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 3)


class FollowingListTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:user:following_list'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        self.users = []
        for i in range(3):
            user = User.objects.create_user(
                username=f'user_{i}',
                password=f'super_secure_{i}',
            )
            self.user.user_profile.followees.add(user)
            self.users.append(user)
        self.url = self.get_url(**self.get_kwargs())

    def test_number_of_followers(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 3)


class FollowUnfollowUserTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:user:follow_unfollow_user'
    methods = ['POST', 'DELETE']

    def get_kwargs(self):
        return {
            'pk': self.other_user.id,
        }

    def setUp(self):
        super().setUp()
        self.url = self.get_url(**self.get_kwargs())

    def test_follow_user(self):
        self.authorize()
        response = self.client.post(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(self.user.user_profile.followees.count(), 1)

    def test_unfollow_user(self):
        self.user.user_profile.followees.add(self.other_user)
        self.authorize()
        response = self.client.delete(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(self.user.user_profile.followees.count(), 0)


class FriendsListTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:user:friend_list'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        FriendRequest.objects.create(
            requester=self.user,
            receiver=self.other_user,
            status='accepted',
        )
        self.url = self.get_url(**self.get_kwargs())

    def test_list_friends(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 1)


class FriendRequestListTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:user:friend_requests_list'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        FriendRequest.objects.create(
            requester=self.other_user,
            receiver=self.user,
            status='pending',
        )
        self.url = self.get_url(**self.get_kwargs())

    def test_list_open_friend_requests(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 1)


class SendFriendRequestTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:user:send_friend_request'
    methods = ['POST']

    def get_kwargs(self):
        return {
            'pk': self.other_user.id,
        }

    def setUp(self):
        super().setUp()
        self.url = self.get_url(**self.get_kwargs())

    def test_send_friend_request(self):
        self.authorize()
        response = self.client.post(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(self.user.connections.count(), 1)
        self.assertEquals(len(mail.outbox), 1)


class PendingFriendRequestListTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:user:pending_friend_request_list'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        FriendRequest.objects.create(
            requester=self.user,
            receiver=self.other_user,
            status='pending'
        )
        self.url = self.get_url(**self.get_kwargs())

    def test_list_friend_requests(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 1)


class AcceptFriendRequestTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:user:accept_friend_request'
    methods = ['POST']

    def get_kwargs(self):
        return {
            'pk': self.friend_request.id,
        }

    def setUp(self):
        super().setUp()
        self.friend_request = FriendRequest.objects.create(
            requester=self.other_user,
            receiver=self.user,
            status='pending'
        )
        self.url = self.get_url(**self.get_kwargs())

    def test_accept_friend_request(self):
        self.authorize()
        response = self.client.post(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(self.user.friend_requests.all()[0].status, 'accepted')


class RejectFriendRequestTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:user:reject_friend_request'
    methods = ['POST']

    def get_kwargs(self):
        return {
            'pk': self.friend_request.id,
        }

    def setUp(self):
        super().setUp()
        self.friend_request = FriendRequest.objects.create(
            requester=self.other_user,
            receiver=self.user,
            status='pending'
        )
        self.url = self.get_url(**self.get_kwargs())

    def test_reject_friend_request(self):
        self.authorize()
        response = self.client.post(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(self.user.friend_requests.all()[0].status, 'rejected')
