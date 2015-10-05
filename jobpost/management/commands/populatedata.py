from django.core.management.base import BaseCommand

from jobpost.models import Address, AddressType, Plan, Employer, EmployerAddress


class Command(BaseCommand):
    help = 'Populate database data!'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        """Populate default database data"""
        # Todo: generate those data from json file
        # populate Plan data
        plans = [Plan(name='Basic', fee=99.99, description='This is basic plan.'),
                 Plan(name='Medium', fee=199.99, description='This is medium plan.'),
                 Plan(name='Premium', fee=299.99, description='This is premium plan'),
                 Plan(name='Free', fee=0.0, description='Free plan means no plan for employer')]

        for plan in plans:
            if plan not in Plan.objects.all():
                plan.save()
            else:
                print str(plan.name) + ' is alredy in database.'

        # populate Address type data
        address_type_list = [AddressType(code='Home', description='This is home address'),
                             AddressType(code='Work', description='This is work address'),
                             AddressType(code='Delivery', description='This is delivery address')]
        for add in address_type_list:
            if add not in AddressType.objects.all():
                add.save()
            else:
                print str(add.code) + ' is already in database.'

        # populate Address data
        add_list = [Address(address_line1='210 Calderon Ave. Apt 210', city='Mountain View', country_state='CA',
                            country_id='USA', zipcode='94034'),
                    Address(address_line1='1035 Aster Ave. Apt 2137', city='Sunnyvale', country_state='CA',
                            country_id='USA', zipcode='94086'),
                    Address(address_line1='10 De Sabla Rd. Unit 407', city='San Mateo', country_state='CA',
                            country_id='USA', zipcode='94402')]
        for add in add_list:
            if not Address.objects.filter(address_line1=add.address_line1):
                add.save()
            else:
                print add.address_line1 + " is already in database"

        # populate Employer
        employers = [Employer(email='zzz@gmail.com', employer_name='VMware', plan=Plan.objects.filter(name='Free')[0]),
                     Employer(email='sadfsdf@gmail.com', employer_name='Facebook', plan=Plan.objects.all()[1]),
                     Employer(email='google@gmail.com', employer_name='Google', plan=Plan.objects.all()[2])]
        for emp in employers:
            if not Employer.objects.filter(employer_name=emp.employer_name):
                emp.save()

        emp_adds = [EmployerAddress(employer=Employer.objects.all()[0], address=Address.objects.all()[0],
                                    address_type=AddressType.objects.all()[0]),
                    EmployerAddress(employer=Employer.objects.all()[1], address=Address.objects.all()[1],
                                    address_type=AddressType.objects.all()[1]),
                    EmployerAddress(employer=Employer.objects.all()[2], address=Address.objects.all()[2],
                                    address_type=AddressType.objects.all()[2])]
        for emp_add in emp_adds:
            emp_add.save()
