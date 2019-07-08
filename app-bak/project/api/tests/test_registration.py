from django.contrib.auth import get_user_model
from django.core import mail
from rest_framework import status

from project.api.tests.master_tests import MasterTestWrapper

User = get_user_model()


class RegistrationTests(MasterTestWrapper.BasicMasterTests):
    endpoint = 'api:registration:registration'
    methods = ['POST']

    def setUp(self):
        self.url = self.get_url(**self.kwargs)

    def test_user_registration(self):
        email = 'test@test.com'
        response = self.client.post(self.url, {
            'email': email
        })
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(mail.outbox), 1)
        user = User.objects.first()
        self.assertIn(user.user_profile.code, mail.outbox[0].body)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_active)
        self.assertEqual(user.username, email)
        self.assertEqual(user.email, email)


class RegistrationValidationTests(MasterTestWrapper.BasicMasterTests):
    endpoint = 'api:registration:registration_validation'
    methods = ['POST']

    def setUp(self):
        self.user = User.objects.create_user(
            username='test@test.com',
            email='test@test.com',
            password='super_secure',
            is_active=False,
        )
        self.url = self.get_url(**self.kwargs)

    def test_user_registration_validation(self):
        email = 'test@test.com'
        response = self.client.post(self.url, {
            'email': email,
            'code': self.user.user_profile.code,
            'password': 'test',
            'password_repeat': 'test',
            'first_name': 'Albert',
            'last_name': 'Einstein',
        })
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        user = User.objects.first()
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.first_name, 'Albert')
        self.assertEqual(user.last_name, 'Einstein')
