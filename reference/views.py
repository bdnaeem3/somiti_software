from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from loan.models import Loan
from installment.models import LoanInstallment
from . forms import ReferenceForm
from . models import Reference
import datetime


@login_required
def add(request):

    if request.method == 'POST':
        form = ReferenceForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            messages.success(request, f'Loan created successfully for {name}')
            form.save()
            return redirect('dashboard')

    else:
        form = ReferenceForm()

    context = {
        'form': form
    }

    return render(request, 'reference/add.html', context)


@login_required
def list(request):

    reference = Reference.objects.all()

    return render(request, 'reference/list.html', {'references': reference})


@login_required
def profile(request, id):

    reference = Reference.objects.get(id=id)

    due = []

    ls = Loan.objects.filter(reference=id)

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
        l.overdue = week_passed - k.count()
        l.loan_paid = loan_paid
        l.current_week = current_week
        l.start_week = start_week

        due.append(l)

    context = {
        'title': 'Reference Profile',
        'reference': reference,
        'loans': due,
    }

    return render(request, 'reference/profile.html', context)
