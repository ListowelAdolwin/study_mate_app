from django.test import SimpleTestCase
from django.urls import resolve, reverse
from baseapp.views import *

class TestUrls(SimpleTestCase):
    """
    This tests the urls of the baseapp project
    """

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, loginPage)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logoutPage)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, registerPage)

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_room_url_resolves(self):
        url = reverse('room', args=['room_slug'])
        self.assertEqual(resolve(url).func, room)

    def test_create_room_url_resolves(self):
        url = reverse('create_room')
        self.assertEqual(resolve(url).func, create_room)

    def test_update_room_url_resolves(self):
        url = reverse('update_room', args=['room_slug'])
        self.assertEqual(resolve(url).func, update_room)

    def test_delete_room_url_resolves(self):
        url = reverse('delete-room', args=['room_slug'])
        self.assertEqual(resolve(url).func, deleteRoom)

    def test_delete_message_url_resolves(self):
        url = reverse('delete-message', args=['room_slug'])
        self.assertEqual(resolve(url).func, deleteMessage)

    def test_profile_url_resolves(self):
        url = reverse('user-profile', args=['room_slug'])
        self.assertEqual(resolve(url).func, userProfile)

    def test_update_profile_url_resolves(self):
        url = reverse('update_profile')
        self.assertEqual(resolve(url).func, edit_profile)

    def test_join_room_url_resolves(self):
        url = reverse('join_room', args=['room_slug'])
        self.assertEqual(resolve(url).func, join_room)

    def test_save_url_resolves(self):
        url = reverse('save', args=['room_slug'])
        self.assertEqual(resolve(url).func, save)

    def test_bookmarks_url_resolves(self):
        url = reverse('bookmarks', args=['room_slug'])
        self.assertEqual(resolve(url).func, bookmarks)

