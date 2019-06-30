from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from savings.models import Savings
from installment.models import LoanInstallment
from django.db.models import Sum

from rest_framework.views import APIView
from rest_framework.response import Response
from loan.models import Loan
from .serializers import loanSerializers


class loan_listing(APIView):

    def get(self, request):
        loan = Loan.objects.all()
        serialize = loanSerializers(loan, many=True)
        return Response(serialize.data)

    def post(self):
        pass


def login(request):
    return render(request, 'login.html')


@login_required
def dashboard(request):

    s = Savings.objects.all()
    l = Loan.objects.all()

    total_savings_person = s.count()
    total_loan_person = l.count()
    total_savings_amount = Savings.objects.aggregate(Sum('amount'))

    total_loan_amount = Loan.objects.aggregate(Sum('amount'))
    loan_after_interest = total_loan_amount['amount__sum'] * 1.2

    total_loan_paid = 0

    for n in l:
        i = LoanInstallment.objects.filter(name=n.id)
        amount = (int(n.amount) *1.2) / 12
        total_loan_paid += i.count() * int(amount)

    loan_due = loan_after_interest - total_loan_paid


    context = {
        'title': 'Dashboard',
        'total_savings': total_savings_person,
        'total_savings_amount': total_savings_amount['amount__sum'],
        'total_loan_person': total_loan_person,
        'total_loan_amount': loan_due
    }

    return render(request, 'dashboard.html', context)


@login_required
def profile(request):
    return render(request, 'profile.html')
