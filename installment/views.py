from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from installment.forms import LoanInstallmentForm, SavingsInstallmentForm


@login_required
def loan_installment(request):

    if request.method == 'POST':
        form = LoanInstallmentForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            messages.success(request, f'Savings account created successfully for {name}')
            form.save()

            return redirect('dashboard')

    else:
        form = LoanInstallmentForm()

    context = {
        'form': form
    }

    return render(request, 'installments/loan.html', context)


@login_required
def savings_installment(request):

    if request.method == 'POST':
        form = SavingsInstallmentForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            messages.success(request, f'Savings account created successfully for {name}')
            form.save()

            return redirect('dashboard')

    else:
        form = SavingsInstallmentForm()

    context = {
        'form': form
    }

    return render(request, 'installments/savings.html', context)
