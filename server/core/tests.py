from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate
from django.contrib.auth.models import User
from core.models import UserProfile, Project


class UserModelTestCase(TestCase):

    def test_will_create_user_profile(self):
        test_user = User(username='test', email='t@t.co', password='hunter2')
        test_user.save()
        test_user_profile = UserProfile.objects.get(user_id=test_user.id)

        self.assertEqual(test_user.id, test_user_profile.user_id)
        self.assertEqual(test_user_profile.bio, 'Hello!')


class UserViewTestCase(APITestCase):

    def setUp(self):
        self.username = 'test'
        self.email = 't@t.co'
        self.password = 'hunter2'
        test_user = User(username=self.username,
                         email=self.email,
                         password=self.password)
        test_user.save()

        self.client.force_authenticate(user=test_user)

    def test_can_retrieve_all_users(self):
        resp = self.client.get(reverse('user-list'))

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data[0]['username'], self.username)
        self.assertEqual(resp.data[0]['bio'], 'Hello!')

    def test_can_retrieve_single_user(self):
        uri = reverse('user-detail', kwargs={'username': self.username})
        resp = self.client.get(uri)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['username'], self.username)
        self.assertEqual(resp.data['bio'], 'Hello!')

    def test_can_update_profile(self):
        uri = reverse('user-detail', kwargs={'username': self.username})
        data = {'bio': 'Updating bio for test user!'}
        resp = self.client.patch(uri, data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['bio'], data['bio'])
