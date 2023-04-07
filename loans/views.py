from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


from .serializers import LoanSerializer, AccountNumberSerializer
from .models import Loan
from customers.models import Customer
from validations.models import Validation

# Create your views here.


@api_view(["POST"])
def get_loans(request, *args, **kwargs):
    """
    Get Loans
    """
    # Get serializer data
    account_number_serializer = AccountNumberSerializer(data=request.data)

    # validate serializer data
    if account_number_serializer.is_valid(raise_exception=True):
        # get valid account number
        account_number = account_number_serializer.validated_data.get(
            'account_number')

        # get customer with account number
        customer = Customer.objects.filter(
            account_number=account_number).first()

        # check if customer exists
        if customer is not None:
            save_validation_request(account_number, "success")
            # get customer loans
            loans = Loan.objects.filter(customer=customer)
            # check if he has any loans
            if loans.count() > 0:
                # return loans
                data = LoanSerializer(loans, many=True).data
                return Response({"loans": data})
            return Response({"message": "No loan found"}, status=200)
        save_validation_request(account_number, "failed")
        return Response({"error": "Customer does not exist"}, status=404)
    return Response({"error": "Fill all required fields"}, status=400)


def save_validation_request(account_number, status):
    Validation.objects.create(account_number=account_number, status=status)


def view_dashboard(request):
    validation_requests = Validation.objects.all()
    total_requests = Validation.objects.count()
    failed_requests = Validation.objects.filter(status='failed').count()
    successful_request = Validation.objects.filter(status='success').count()

    context = {
        "validation_requests": validation_requests,
        "total_requests": total_requests,
        "failed_requests": failed_requests,
        "successful_request": successful_request
    }

    return render(request, 'index.html', context)
