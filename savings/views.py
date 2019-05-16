from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import SavingsForm
from . models import Savings
from reference.models import Reference
from installment.models import SavingsInstallment
import datetime


@login_required
def add(request):

    if request.method == 'POST':
        form = SavingsForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            mobile = form.cleaned_data.get('mobile')
            nid = form.cleaned_data.get('nid')
            messages.success(request, f'Savings account created successfully for {name}')

            r = Reference(name=name, address=address, mobile=mobile, nid=nid)
            form.save()

            r.save()

            return redirect('dashboard')

    else:
        form = SavingsForm()

    context = {
        'form': form
    }

    return render(request, 'savings/add.html', context)


@login_required
def list(request):

    due = []

    ls = Savings.objects.all()

    for l in ls:
        current_week = datetime.datetime.utcnow().isocalendar()[1]
        start_week = datetime.date(l.join_date.year, l.join_date.month, l.join_date.day).isocalendar()[1]

        if current_week > 33:
            current_week -= 33
            start_week -= 33
        else:
            current_week += 19
            start_week += 19

        k = SavingsInstallment.objects.filter(name=l.id)
        week_passed = current_week - start_week
        savings_paid = k.count()
        overdue = week_passed - k.count()
        l.total = l.amount * k.count()
        l.overdue = overdue
        l.savings_paid = savings_paid
        l.current_week = current_week
        l.start_week = start_week
        due.append(l)

        # due.append([l, overdue])
        # for h in k:
        #     w = datetime.date(h.pay_date.year, h.pay_date.month, h.pay_date.day).isocalendar()[1] - 33
        #     # total_missing = 12 - l.loaninstallment_set.count()
        #     # overdue = total_missing
        #     while start_week < current_week and start_week != w and  <= 12:
        #         # print(str(l.name) + ' has not paid loan in week no ' + str(start_week))
        #         due.append(l)
        #         start_week += 1

    context = {
        'savings': due
    }

    return render(request, 'savings/list.html', context)


@login_required
def profile(request, id):

    savings = Savings.objects.get(id=id)

    i = SavingsInstallment.objects.filter(name=id)

    current_week = datetime.datetime.utcnow().isocalendar()[1]
    start_week = datetime.date(savings.join_date.year, savings.join_date.month, savings.join_date.day).isocalendar()[1]

    if current_week > 33:
        current_week -= 33
        start_week -= 33
    else:
        current_week += 19
        start_week += 19

    week_passed = current_week - start_week
    savings_paid = i.count()
    overdue = week_passed - i.count()

    context = {
        'title': 'Savings Profile',
        'savings': savings,
        'ins': i,
        'overdue': overdue,
        'week_passed': week_passed,
        'savings_paid': savings_paid
    }

    return render(request, 'savings/profile.html', context)
