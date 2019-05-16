from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name='loan_add'),
    path('list', views.list, name='loan_list'),
    path('profile/<int:id>', views.profile, name='loan_profile'),
]
