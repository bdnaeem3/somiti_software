from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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

    context = {
        'title': 'Dashboard'
    }

    return render(request, 'dashboard.html', context)


@login_required
def profile(request):
    return render(request, 'profile.html')
