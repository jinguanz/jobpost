from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('Users must have email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user


class BaseUser(AbstractBaseUser):
    """Base User"""
    email = models.EmailField(verbose_name='Email address', max_length=200, unique=True)
    is_staff = models.BigIntegerField(default=True, blank=True)
    USERNAME_FIELD = 'email'

    objects = UserManager()
