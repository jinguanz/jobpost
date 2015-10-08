from django.db import models
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel


# Create your models here.
class Address(TimeStampedModel):
    address_line1 = models.CharField(max_length=200, blank=False)
    address_line2 = models.CharField(max_length=200)
    address_line3 = models.CharField(max_length=200)
    city = models.CharField(max_length=200, blank=False)
    country_state = models.CharField(max_length=200, blank=False)
    zipcode = models.CharField(max_length=200, blank=False)
    country_id = models.CharField(max_length=200, blank=False)
    other_address_details = models.CharField(max_length=400, blank=True)

    def __unicode__(self):
        return '{0}'.format(self.address_line1)


class AddressType(TimeStampedModel):
    """
    This is model for address type, home, work, delivery
    """
    code = models.CharField(max_length=200, null=False, blank=False, primary_key=True)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return '{0}'.format(self.code)


class Plan(models.Model):
    """
    This is service plan model
    """
    name = models.CharField(max_length=200, blank=False, primary_key=True)
    fee = models.FloatField(blank=False, default=0.0)
    description = models.TextField()

    def __unicode__(self):
        return '{0}'.format(self.name)


class Account(TimeStampedModel):
    """
    This is abstract user account model
    """
    email = models.EmailField()
    tel_country_code = models.CharField(max_length=10, blank=False, default='01')
    tel_area_code = models.CharField(max_length=10, blank=False)
    tel_remain = models.CharField(max_length=200, blank=False)

    class Meta:
        abstract = True


class Employer(Account):
    """
    This is employer model
    """
    employer_name = models.CharField(max_length=200, blank=False)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    default_email_contact = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_register = models.BooleanField(default=False)
    auto_register = models.BooleanField(default=True)
    register_start_date = models.DateField(null=True)
    register_end_date = models.DateField(null=True)

    @property
    def phone_number(self):
        return '(' + str(self.tel_country_code) + ')' + self.tel_area_code + self.tel_remain

    def __unicode__(self):
        return '{0}'.format(self.employer_name)

    def get_absolute_url(self):
        return reverse('employers:detail', kwargs={'pk': self.pk})


class CreditCard(TimeStampedModel):
    """
    This is model to save credit card information
    """
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    holder_name = models.CharField(max_length=200)
    number = models.CharField(max_length=16)
    security_code = models.CharField(max_length=3)
    expiration_date_month = models.CharField(max_length=2)
    expiration_date_year = models.CharField(max_length=4)
    is_default = models.BooleanField(default=False)

    def __unicode__(self):
        return '{0} {1}'.format(self.type, self.holder_name)


class Candidate(Account):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    resume = models.FileField(upload_to='resume/%Y/%m/%d', blank=True)

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class EmployerAddress(TimeStampedModel):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    address_type = models.ForeignKey(AddressType, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('address', 'address_type', 'employer'),)

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.address.address_line1, self.address_type.code, self.employer.employer_name)


class CandidateAddress(TimeStampedModel):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    address_type = models.ForeignKey(AddressType, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('address', 'address_type', 'candidate'),)

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.address.address_line1, self.address_type.code, self.candidate.first_name)


class Job(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    link = models.URLField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)

    def __unicode__(self):
        return '{0} {1}'.format(self.title, self.employer.employer_name)

    def get_absolute_url(self):
        return reverse('employers:job_detail', kwargs={'pk': self.pk})


class JobClick(TimeStampedModel):
    """
     This is model to track job click information
    """
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    # anonymous user click without candidate id
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, blank=True, null=True)

    def __unicode__(self):
        return '{0} {1}'.format(self.job.title, self.job.employer.employer_name)


class Payment(TimeStampedModel):
    """
    This is model to track payment information
    """
    employer = models.ForeignKey(Employer, on_delete=models.PROTECT)
    card = models.ForeignKey(CreditCard, on_delete=models.PROTECT)
    description = models.TextField()
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)

    def __unicode__(self):
        return '{0} {1}'.format(self.employer.employer_name, self.description)
