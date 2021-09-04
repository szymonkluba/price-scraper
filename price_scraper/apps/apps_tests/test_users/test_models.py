from apps.users.models import CustomUser
from django.test import TestCase


class UserManagerTests(TestCase):

    def test_create_user(self):
        user = CustomUser.objects.create_user(
            email='test@example.com', password='testPassword')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            CustomUser.objects.create_user()
        with self.assertRaises(TypeError):
            CustomUser.objects.create_user(email='')
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(email='', password='testPassword')

    def test_create_superuser(self):
        admin_user = CustomUser.objects.create_superuser(
            email='test_superuser@example.com', password='testPassword')
        self.assertEqual(admin_user.email, 'test_superuser@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                email='test_superuser@example.com', password='testPassword', is_superuser=False)
