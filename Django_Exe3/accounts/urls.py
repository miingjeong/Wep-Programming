from django.urls import path
from . import views

urlpatterns=[
    path('sigh_up/', views.sign_up, name='sign_up')
]