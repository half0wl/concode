from django.test import TestCase
from django.contrib.auth.models import User
from core.models import UserProfile, Project


class UserTest(TestCase):

    def test_will_create_user_profile(self):
        test_user = User(username='test', email='t@t.co', password='hunter2')
        test_user.save()
        test_user_profile = UserProfile.objects.get(user_id=test_user.id)

        self.assertEqual(test_user.id, test_user_profile.user_id)
        self.assertEqual(test_user_profile.bio, 'Hello!')
