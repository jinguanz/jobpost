__author__ = 'jinguangzhou'
from django.test import TestCase, Client

from .models import EmployerUser, CandidateUser


class LoginTest(TestCase):
    def setUp(self):
        # create employer user
        emp = EmployerUser.objects.create(email='emp_test@gmail.com', company_name='test_company')
        # set hash password
        emp.set_password('test')
        emp.save()
        can = CandidateUser.objects.create(email='can_test@gmail.com', first_name='first_test', last_name='last_test')
        can.set_password('test')
        can.save()
        self.client = Client()

    def test_employer_login(self):
        get_response = self.client.get('/employers/login/')
        self.assertEqual(get_response.status_code, 200,
                         'We expect return code is {0} but real code is {1}'.format(200, get_response.status_code))
        is_login = self.client.login(email='emp_test@gmail.com', password='test')
        is_login_fail = self.client.login(email='emp@gmail.com', password='test')
        self.assertEqual(is_login, True,
                         'We expect return code is {0} but real code is {1}'.format(True, is_login))
        self.assertEqual(is_login_fail, False, 'Expected {0} but real is {1}'.format(False, is_login_fail))

    def test_candidate_lgoin(self):
        response = self.client.get('/candidates/login/')
        self.assertEqual(response.status_code, 200,
                         'We expect return code is {0} but real code is {1}'.format(200, response.status_code))
        is_login = self.client.login(email='can_test@gmail.com', password='test')
        is_login_fail = self.client.login(email='can_test@gmail.com', password='test01')
        self.assertEqual(is_login, True,
                         'We expect return code is {0} but real code is {1}'.format(True, is_login))
        self.assertEqual(is_login_fail, False, 'Expected is {0} but real is {1}'.format(False, is_login_fail))

    def test_login_redirect(self):
        emp_response = self.client.get('/employers/dashboard/')
        self.assertRedirects(emp_response, '/employers/login/?next=/employers/dashboard/')
        can_response = self.client.get('/candidates/dashboard/')
        self.assertRedirects(can_response, '/candidates/login/?next=/candidates/dashboard/')


class JobTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_jobs_page(self):
        response = self.client.get('/jobs/')
        self.assertEqual(response.status_code, 200,
                         'We expect return code is {0} but real is {1}'.format(200, response.status_code))

# class UserRegistrationTest(TestCase):
#     def setUp(self):
#         pass
#
#     def test_employer_registration(self):
#         """
#         Test employer registration
#         :return:
#         """
#         response = self.client.post('/employers/registration/', {'email': 'test_emp@gmail.com', 'company_name': 'test', 'password1': 'test', 'password2': 'test'})
#         print response
#         self.assertEqual(response.status_code, 200)
