from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.urlresolvers import reverse

from core.models import BaseUser


# http://www.lasolution.be/blog/creating-custom-user-model-django-16-part-2.html

# Create your models here.
class EmployerUserManager(BaseUserManager):
    def create_user(self, email, company_name, password=None):
        if not email:
            raise ValueError('Users must have email address')

        user = self.model(email=self.normalize_email(email), company_name=company_name)
        user.set_password(password)
        user.save()
        return user


class EmployerUser(BaseUser, PermissionsMixin):
    company_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, blank=True)

    objects = EmployerUserManager()

    # USERNAME_FIELD = 'email'

    def __str__(self):
        return self.company_name + self.email

    def get_absolute_url(self):
        return reverse('employer:detail', kwargs={'pk': self.pk})
