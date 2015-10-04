from django.db import models

from model_utils.models import TimeStampedModel


# Create your models here.
class Address(TimeStampedModel):
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200, blank=False)
    address_line3 = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, blank=False)
    country_state = models.CharField(max_length=200, blank=False)
    zipcode = models.CharField(max_length=200, blank=False)
    country_id = models.CharField(max_length=200, blank=False)
    other_address_details = models.CharField(max_length=400, blank=True)


class AddressType(TimeStampedModel):
    """
    This is model for address type, home, work, delivery
    """
    code = models.CharField(max_length=200, null=False, blank=False, primary_key=True)
    description = models.CharField(max_length=200)


class Plan(models.Model):
    """
    This is service plan model
    """
    name = models.CharField(max_length=200, blank=False, primary_key=True)
    fee = models.FloatField(blank=False, default=0.0)
    description = models.TextField()


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
    plan = models.ForeignKey(Plan, null=True, on_delete=models.SET_NULL)
    default_email_contact = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_register = models.BooleanField(default=False)
    auto_register = models.BooleanField(default=True)
    register_start_date = models.DateField(null=True)
    register_end_date = models.DateField(null=True)
    # todo: more fields to handle payment


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


class Candidate(Account):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    resume = models.FileField(upload_to='resume/%Y/%m/%d')


class EmployerAddress(TimeStampedModel):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    address_type = models.ForeignKey(AddressType, on_delete=models.SET_NULL, null=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)


class CandidateAddress(TimeStampedModel):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    address_type = models.ForeignKey(AddressType, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)


class Job(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    link = models.URLField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)


class JobClick(TimeStampedModel):
    """
     This is model to track job click information
    """
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    # anonymous user click without candidate id
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, blank=True, null=True)


class Payment(TimeStampedModel):
    """
    This is model to track payment information
    """
    employer = models.ForeignKey(Employer, on_delete=models.PROTECT)
    card = models.ForeignKey(CreditCard, on_delete=models.PROTECT)
    description = models.TextField()
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
