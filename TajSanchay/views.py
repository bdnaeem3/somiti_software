from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
