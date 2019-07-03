from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from savings.models import Savings
from installment.models import LoanInstallment
from loan.models import Loan

# def login(request):
#     return render(request, 'login.html')


@login_required
def dashboard(request):

    sv = Savings.objects.all()
    ls = Loan.objects.all()

    total_savings_person = sv.count()
    total_loan_person = ls.count()

    total_savings_amount = 0
    for s in sv:
        total_savings_amount += int(s.amount)


    total_loan_amount = 0
    for l in ls:
        total_loan_amount += int(l.amount)

    loan_after_interest = total_loan_amount * 1.2

    total_loan_paid = 0

    for n in ls:
        i = LoanInstallment.objects.filter(name=n.id)
        amount = (int(n.amount) *1.2) / 12
        total_loan_paid += i.count() * int(amount)

    loan_due = loan_after_interest - total_loan_paid


    context = {
        'title': 'Dashboard',
        'total_savings': total_savings_person,
        'total_savings_amount': total_savings_amount,
        'total_loan_person': total_loan_person,
        'total_loan_amount': int(loan_due)
    }

    return render(request, 'dashboard.html', context)


@login_required
def profile(request):
    return render(request, 'profile.html')
