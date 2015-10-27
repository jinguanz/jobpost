from django.contrib import admin

from .models import Address, AddressType, Plan, EmployerAddress, CandidateAddress, Job, JobClick, \
    Payment, CreditCard

# Register your models here.
admin.site.register(Address)
admin.site.register(AddressType)
admin.site.register(Plan)
admin.site.register(EmployerAddress)
admin.site.register(CandidateAddress)
admin.site.register(Job)
admin.site.register(JobClick)
admin.site.register(Payment)
admin.site.register(CreditCard)
