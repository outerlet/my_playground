from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('another/', views.another, name='another'),
    path('login/', views.login, name='login'),
    path('publisher/', views.publisher, name='publisher'),
]
