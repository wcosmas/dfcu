from django.db import models
from customers.models import Customer

# Create your models here.


STATUS = (
    ("success", "success"),
    ("failed", "failed"),
)


class Validation(models.Model):
    account_number = models.CharField(max_length=100)
    status = models.CharField(
        max_length=50,
        choices=STATUS,
        default='success'
    )
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.customer.first_name+" "+self.customer.last_name
