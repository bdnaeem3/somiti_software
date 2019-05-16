from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name='savings_add'),
    path('list', views.list, name='savings_list'),
    path('profile/<int:id>', views.profile, name='savings_profile'),
]
