from django.urls import path
from . import views

urlpatterns=[
    path('my_page/',views.my_page, name='my_page'),

    path('word_count/',views.word_count, name='word_count')

]