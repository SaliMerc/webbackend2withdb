from django.urls import path
from .import views

urlpatterns=[
    path('',views.insert,name='my_insert'),

]