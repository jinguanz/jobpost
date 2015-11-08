__author__ = 'jinguangzhou'
from django.test import TestCase

from .models import CandidateUser
from .forms import CandidateUserCreationUserForm


class CandidateFormTest(TestCase):
    def setUp(self):
        can = CandidateUser(email='test_can@gmail.com', first_name='first', last_name='last')
        can.set_password('test')
        can.save()

    def test_candidate_form_valid(self):
        """
        Test candidate form with valid input
        :return:
        """
        form_data = {'email': 'test1_can@gmail.com', 'first_name': 'first', 'last_name': 'last', 'password1': 'test',
                     'password2': 'test'}
        form = CandidateUserCreationUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_candidate_form_with_existing_email(self):
        """
        Test candidate form with existing email input
        :return:
        """
        form_data = {'email': 'test_can@gmail.com', 'first_name': 'first', 'last_name': 'last', 'password1': 'test',
                     'password2': 'test'}
        form = CandidateUserCreationUserForm(data=form_data)
        expected_error = 'Base user with this Email address already exists.'
        real_error = []
        for key, value in form.errors.items():
            for error in value:
                real_error.append(error)
        self.assertFalse(form.is_valid())
        self.assertTrue(len(real_error) == 1, 'We expect one error message but real is {0}'.format(len(real_error)))
        self.assertTrue(real_error[0], expected_error)

    def test_candidate_form_with_different_password(self):
        """
        Test candidate form with different password
        :return:
        """
        form_data = {'email': 'test5_can@gmail.com', 'first_name': 'first', 'last_name': 'last', 'password1': 'test',
                     'password2': 'different_password'}
        form = CandidateUserCreationUserForm(data=form_data)
        expected_error = 'The two password fields didn\'t match.'
        real_error = []
        for key, value in form.errors.items():
            for error in value:
                real_error.append(error)
        self.assertFalse(form.is_valid())
        self.assertTrue(len(real_error) == 1, 'We expect one error message but real is {0}'.format(len(real_error)))
        self.assertTrue(real_error[0], expected_error)

    def test_candidate_form_blank_email(self):
        """
        Test candidate form with blank email
        :return:
        """
        form_data = {'email': '', 'first_name': 'first', 'last_name': 'last', 'password1': 'test',
                     'password2': 'test'}
        form = CandidateUserCreationUserForm(data=form_data)
        expected_error = 'This field is required.'
        real_error = []
        for key, value in form.errors.items():
            for error in value:
                real_error.append(error)
        self.assertFalse(form.is_valid())
        self.assertTrue(len(real_error) == 1, 'We expect one error message but real is {0}'.format(len(real_error)))
        self.assertTrue(real_error[0], expected_error)

    def test_candidate_form_blan_first_name(self):
        """
        Test candidate form with blank first name
        :return:
        """
        form_data = {'email': 'test6_can@gmail.com', 'first_name': '', 'last_name': 'last', 'password1': 'test',
                     'password2': 'test'}
        form = CandidateUserCreationUserForm(data=form_data)
        expected_error = 'This field is required.'
        real_error = []
        for key, value in form.errors.items():
            for error in value:
                real_error.append(error)
        self.assertFalse(form.is_valid())
        self.assertTrue(len(real_error) == 1, 'We expect one error message but real is {0}'.format(len(real_error)))
        self.assertTrue(real_error[0], expected_error)

    def test_candidate_form_blan_last_name(self):
        """
        Test candidate form with blank first name
        :return:
        """
        form_data = {'email': 'test6_can@gmail.com', 'first_name': 'first', 'last_name': '', 'password1': 'test',
                     'password2': 'test'}
        form = CandidateUserCreationUserForm(data=form_data)
        expected_error = 'This field is required.'
        real_error = []
        for key, value in form.errors.items():
            for error in value:
                real_error.append(error)
        self.assertFalse(form.is_valid())
        self.assertTrue(len(real_error) == 1, 'We expect one error message but real is {0}'.format(len(real_error)))
        self.assertTrue(real_error[0], expected_error)
