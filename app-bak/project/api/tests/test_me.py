from django.contrib.auth import get_user_model
from rest_framework import status

from project.api.tests.master_tests import MasterTestWrapper

User = get_user_model()


class GetUpdateUserProfileTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:me:get_update_user_profile'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        self.url = self.get_url(**self.get_kwargs())

    def test_get_user_profile(self):
        self.authorize()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('username'), self.user.username)
        self.assertEquals(response.data.get('email'), self.user.email)
        self.assertEquals(response.data.get('first_name'), self.user.first_name)
        self.assertEquals(response.data.get('last_name'), self.user.last_name)

    def test_update_user_profile(self):
        self.authorize()
        username = 'new_username'
        response = self.client.post(self.url, {
            'username': username,
            'first_name': 'Alberto',
            'last_name': 'Zweistein',
        })
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(pk=self.user.pk)
        self.assertEquals(user.username, username)
        self.assertEquals(user.first_name, 'Alberto')
        self.assertEquals(user.last_name, 'Zweistein')

    def test_update_existing_username(self):
        self.authorize()
        response = self.client.post(self.url, {
            'username': 'other_user'
        })
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Username is already taken!', response.data.get('username'))
