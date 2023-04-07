from django.core.management.base import BaseCommand
from loans.factory import LoanFactory
from customers.factory import CustomerFactory


class Command(BaseCommand):
    help = 'Seeds the database with sample data using factory_boy'

    def handle(self, *args, **options):
        num_objects = 10  # Number of objects to create
        for i in range(num_objects):
            LoanFactory.create()
        CustomerFactory.create()
        self.stdout.write(self.style.SUCCESS(
            f'Successfully seeded {num_objects} objects'))
