from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import UserProfile
from waterGIS.forms import LoginForm, UserRegistrationForm, UserProfileUpdateForm

# class ViewTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = get_user_model().objects.create_user(
#             username='testuser', password='12345')
#         self.user_profile = UserProfile.objects.create(
#             user=self.user, is_premium_user='NO')

#     def test_home_view(self):
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code, 200)

#     def test_home2_view_unauthenticated(self):
#         response = self.client.get(reverse('home2'))
#         self.assertEqual(response.status_code, 302)  # Expecting a redirect

#     def test_home2_view_authenticated(self):
#         self.client.login(username='testuser', password='12345')
#         response = self.client.get(reverse('home2'))
#         self.assertEqual(response.status_code, 200)

#     def test_get_user_permission_status_unauthenticated(self):
#         response = self.client.get(reverse('get_user_permission_status'))
#         self.assertEqual(response.status_code, 302)  # Expecting a redirect

#     def test_get_user_permission_status_authenticated(self):
#         self.client.login(username='testuser', password='12345')
#         response = self.client.get(reverse('get_user_permission_status'))
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), {'is_premium_user': False})


# def setUp(self):
#     self.client = Client()
#     self.user = get_user_model().objects.create_user(
#         username='testuser', email='testuser@example.com', password='12345')
#     self.user_profile = UserProfile.objects.create(
#         user=self.user, is_premium_user='NO')

from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile


class ModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', email='testuser@example.com', password='12345')
        self.user_profile = UserProfile.objects.create(
            user=self.user, is_premium_user='NO')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('12345'))

    def test_get_profile_picture(self):
        self.assertEqual(self.user.get_profile_picture(), '')

    def test_user_profile_creation(self):
        self.assertEqual(self.user_profile.user, self.user)
        self.assertEqual(self.user_profile.is_premium_user, 'NO')


class URLTest(TestCase):
    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(url, '/login/')

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(url, '/logout/')

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(url, '/register/')

    def test_profile_url(self):
        url = reverse('profile')
        self.assertEqual(url, '/profile/')

    def test_view_user_information_url(self):
        url = reverse('view_user_information', args=['testuser'])
        self.assertEqual(url, '/view_user_information/testuser/')

    def test_get_user_permission_status_url(self):
        url = reverse('get_user_permission_status')
        self.assertEqual(url, '/get_user_permission_status/')
