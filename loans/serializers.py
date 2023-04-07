from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Loan
from validations.models import Validation


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = '__all__'


class AccountNumberSerializer(serializers.Serializer):
    account_number = serializers.CharField()

    class Meta:
        fields = ['account_number']

    def validate_account_number(self, account_number):
        if len(account_number) <= 0:
            Validation.objects.create(
                account_number='Empty', status='failed')
            raise serializers.ValidationError("Provide account number")
        if len(account_number) != 10:
            Validation.objects.create(
                account_number=account_number, status='failed')
            raise serializers.ValidationError("Invalid number account number")
        return account_number
