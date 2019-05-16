from django.contrib import admin
from . models import LoanInstallment, SavingsInstallment

admin.site.register(LoanInstallment)
admin.site.register(SavingsInstallment)
