from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.first_name+" "+self.last_name
