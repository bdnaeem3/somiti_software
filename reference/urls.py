from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name='reference_add'),
    path('list', views.list, name='reference_list'),
    path('profile/<int:id>', views.profile, name='reference_profile'),
]
