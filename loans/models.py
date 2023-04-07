from django.db import models
from customers.models import Customer

# Create your models here.


class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.customer.first_name+" "+self.customer.last_name
