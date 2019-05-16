from django.urls import path
from . import views

urlpatterns = [
    path('loan', views.loan_installment, name='loan_installments'),
    path('savings', views.savings_installment, name='savings_installments'),
]
