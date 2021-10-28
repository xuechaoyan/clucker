from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import User
from django.db import models

class PostModelTestCase(TestCase):
    def setUp(self):
        self.post=Post.objects.create_post(
            author='Ryan',
            text='this is a text',
            created_at=models.DateTimeFIeld()
        )

    def test_author_must_be_unique(self):
        second_user= self._create_second_user()
        self.user.username = second_user.username
        self._assert_user_is_invalid()

    def _assert_post_is_valid(self):
        try:
            self.psot.full_clean()
        except(ValidationError):
            self.fail('Test user should be valid')


    def _assert_post_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

class UserMOdelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            password='Password123',
            bio='the quick brown fox... '
        )
    def test_valid_user(self):
        self._assert_user_is_valid()

    def test_username_cannot_be_blank(self):
        self.user.username=''
        self._assert_user_is_invalid()

    def test_username_can_be_30_chars_long(self):
        self.user.username='@'+'x'*29
        self._assert_user_is_valid()

    def test_username_cannot_over_30_chars_long(self):
        self.user.username='@'+'x'*30
        self._assert_user_is_invalid()

    def test_username_must_be_unique(self):
        second_user= self._create_second_user()
        self.user.username = second_user.username
        self._assert_user_is_invalid()

    def test_username_start_with_at_symbol(self):
        self.user.username = 'johndoe'
        self._assert_user_is_invalid()

    def test_username_must_contain_only_alphanumericals_after_at(self):
        self.user.username = '@john!doe'
        self._assert_user_is_invalid()

    def test_username_must_contain_at_least_3alphanumericals_after_at(self):
        self.user.username = '@jo'
        self._assert_user_is_invalid()

    def test_username_may_contain_numbers(self):
        self.user.username = '@j0hndoe2'
        self._assert_user_is_valid()

    def test_username_must_contain_at_least_3alphanumericals_after_at(self):
        self.user.username = '@jo'
        self._assert_user_is_invalid()

    def test_username_must_contain_only_one_at(self):
        self.user.username = '@@johndoe'
        self._assert_user_is_invalid()

    def test_first_name_must_not_be_blank(self):
        self.user.first_name=''
        self._assert_user_is_invalid()

    def test_first_name_may_not_be_unique(self):
         second_user = self._create_second_user()
         self.user.first_name=second_user.first_name
         self._assert_user_is_valid()

    def test_first_name_may_contain_50_characters(self):
        self.user.first_name='x'*50
        self._assert_user_is_valid()

    def test_first_name_cannot_over_50_characters(self):
        self.user.first_name='x'*51
        self._assert_user_is_invalid()

    def test_last_name_must_not_be_blank(self):
        self.user.last_name=''
        self._assert_user_is_invalid()

    def test_last_name_may_not_be_unique(self):
         second_user = self._create_second_user()
         self.user.last_name=second_user.last_name
         self._assert_user_is_valid()

    def test_last_name_may_contain_50_characters(self):
        self.user.last_name='x'*50
        self._assert_user_is_valid()

    def test_last_name_cannot_over_50_characters(self):
        self.user.last_name='x'*51
        self._assert_user_is_invalid()

    def test_email_must_not_be_blank(self):
        self.user.email=''
        self._assert_user_is_invalid()

    def test_email_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.email=second_user.email
        self._assert_user_is_invalid()

    def test_email_must_contan_username(self):
        self.user.email='@example.org'
        self._assert_user_is_invalid()

    def test_email_must_contan_at(self):
        self.user.email='johndoe.example.org'
        self._assert_user_is_invalid()

    def test_email_must_contan_domian_name(self):
        self.user.email='johndoe@.org'
        self._assert_user_is_invalid()

    def test_email_must_contan_domian(self):
        self.user.email='johndoe@example'
        self._assert_user_is_invalid()

    def test_email_must_mot_have_more_thab_one_at(self):
        self.user.email='johndoe@@example.org'
        self._assert_user_is_invalid()

    def test_bio_may_be_blank(self):
        self.user.bio=''
        self._assert_user_is_valid()

    def test_bio_does_not_need_to_be_unique(self):
        second_user = self._create_second_user()
        self.user.bio=second_user.bio
        self._assert_user_is_valid()

    def test_bio_contain_520_characters(self):
        self.user.bio='x' *520
        self._assert_user_is_valid()

    def test_bio_cannot_contain_over_520_characters(self):
        self.user.bio='x'*521
        self._assert_user_is_invalid()

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except(ValidationError):
            self.fail('Test user should be valid')


    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def  _create_second_user(self):
         user=User.objects.create_user(
            '@janedoe',
            first_name='Jane',
            last_name='Doe',
            email='janedoe@example.org',
            password='Password123',
            bio='the quick brown fox... ')
         return user
