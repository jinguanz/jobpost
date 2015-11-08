__author__ = 'jinguangzhou'
from django.test import TestCase

from .forms import EmployerUserCreationForm
from .models import EmployerUser


class EmployerFormTest(TestCase):
    def setUp(self):
        emp = EmployerUser.objects.create(email='test_emp@gmail.com', company_name='test')
        emp.set_password('test')
        emp.save()

    def test_employer_create_form(self):
        """
        Test form with valid input
        :return:
        """
        form_data = {'email': 'test1_emp@gmail.com', 'company_name': 'test', 'password1': 'test', 'password2': 'test'}
        form = EmployerUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_employer_create_form_email_invalid(self):
        """
        Test form with existing email address
        :return:
        """
        form_data = {'email': 'test_emp@gmail.com', 'company_name': 'test', 'password1': 'test', 'password2': 'test'}
        form = EmployerUserCreationForm(data=form_data)
        expected_error = 'Base user with this Email address already exists.'
        real_error = None
        for key, value in form.errors.items():
            # value is <class 'django.forms.utils.ErrorList'>
            for error in value:
                real_error = error
                break
            break
        self.assertFalse(form.is_valid())
        self.assertEqual(expected_error, real_error)

    def test_employer_create_from_password_invalid(self):
        """
        Test form with invalid password input
        :return:
        """
        form_data = {'email': 'test2_emp@gmail.com', 'company_name': 'test', 'password1': 'test',
                     'password2': 'wrong_password'}
        form = EmployerUserCreationForm(data=form_data)
        expected_error = 'The two password fields didn\'t match.'
        real_error = []
        for key, value in form.errors.items():
            for error in value:
                real_error.append(error)
        self.assertFalse(form.is_valid())
        self.assertTrue(len(real_error) == 1, 'Expect one error message but real is {0}'.format(len(real_error)))
        self.assertEqual(real_error[0], expected_error)

    def test_employer_create_form_company_name_blank(self):
        """
        Test form with blank company name input
        :return:
        """
        form_data = {'email': 'test3_emp@gmail.com', 'company_name': '', 'password1': 'test',
                     'password2': 'test'}
        form = EmployerUserCreationForm(data=form_data)
        expected_error = 'This field is required.'
        real_error = []
        for key, value in form.errors.items():
            for error in value:
                print error
                real_error.append(error)
        self.assertFalse(form.is_valid())
        self.assertTrue(len(real_error) == 1, 'Expect one error message but real is {0}'.format(len(real_error)))
        self.assertEqual(real_error[0], expected_error)

    def test_employer_create_form_email_blank(self):
        """
        Test form with blank email input
        :return:
        """
        form_data = {'email': '', 'company_name': 'test', 'password1': 'test',
                     'password2': 'test'}
        form = EmployerUserCreationForm(data=form_data)
        expected_error = 'This field is required.'
        real_error = []
        for key, value in form.errors.items():
            for error in value:
                real_error.append(error)
        self.assertFalse(form.is_valid())
        self.assertTrue(len(real_error) == 1, 'Expect one error message but real is {0}'.format(len(real_error)))
        self.assertTrue(real_error[0], expected_error)
