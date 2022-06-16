from django.urls import path

from keiba import views

from . import urls

app_name = 'keiba'

urlpatterns = [
    path('', views.index, name='index'),
]
