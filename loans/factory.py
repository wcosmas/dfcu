import factory
from factory.faker import Faker
from .models import Loan
from customers.models import Customer


class LoanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Loan
    customer = Customer.objects.get_or_create(
        first_name='Wamozo', last_name='Cosmas', phone='0756863683', address='Kayunga', account_number='3459871348')[0]
    amount = factory.Faker('pyfloat', left_digits=5, right_digits=2)
