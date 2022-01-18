from django.urls import path

from . import views

urlpatterns = [
    path('outlets', views.outlets, name='outlets')
]
