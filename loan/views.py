from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from . forms import LoanForm
from . models import Loan
from installment.models import LoanInstallment
import datetime
from django.http import JsonResponse


@login_required
def add(request):

    if request.method == 'POST':
        form = LoanForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            mobile = form.cleaned_data.get('mobile')
            nid = form.cleaned_data.get('nid')
            messages.success(request, f'Loan created successfully for {name}')
            form.save()

            return redirect('dashboard')

    else:
        form = LoanForm()

    context = {
        'form': form,
    }

    return render(request, 'loan/add.html', context)


@login_required
def list(request):

    due = []

    ls = Loan.objects.all()

    for l in ls:
        current_week = datetime.datetime.utcnow().isocalendar()[1]
        start_week = datetime.date(l.join_date.year, l.join_date.month, l.join_date.day).isocalendar()[1]

        if current_week > 33:
            current_week -= 33
            start_week -= 33
        else:
            current_week += 19
            start_week += 19

        k = LoanInstallment.objects.filter(name=l.id)
        week_passed = current_week - start_week
        loan_paid = k.count()
        overdue = week_passed - k.count()

        l.overdue = overdue
        l.loan_paid = loan_paid
        l.current_week = current_week
        l.start_week = start_week

        if (loan_paid + overdue) < 12:
            due.append(l)

    print(current_week)
    print(start_week)

    context = {
        'loans': ls,
    }

    return render(request, 'loan/list.html', context)


@login_required
def profile(request, id):

    loan = Loan.objects.get(id=id)

    i = LoanInstallment.objects.filter(name=id)

    current_week = datetime.datetime.utcnow().isocalendar()[1]
    start_week = datetime.date(loan.join_date.year, loan.join_date.month, loan.join_date.day).isocalendar()[1]

    if current_week > 33:
        current_week -= 33
        start_week -= 33
    else:
        current_week += 19
        start_week += 19

    week_passed = current_week - start_week

    overdue = week_passed - i.count()

    context = {
        'title': 'Loan Profile',
        'loans': loan,
        'ins': i,
        'overdue': overdue,
        'week_passed': week_passed
    }

    return render(request, 'loan/profile.html', context)
