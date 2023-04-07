import factory
from factory.faker import Faker
from customers.models import Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer
    first_name = 'Joshua'
    last_name = 'Joshua'
    account_number = '2348765156'
    address = 'Busabala'
    phone = '072345781'
