from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.core.urlresolvers import reverse

from core.models import BaseUser


# Create your models here.
class CandidateUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user


class CandidateUser(BaseUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CandidateUserManager()

    def get_absolute_url(self):
        return reverse('candidate:detail', kwargs={'pk': self.pk})
