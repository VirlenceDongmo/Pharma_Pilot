from django.urls import path
from Produits import views

urlpatterns = [
    path('', views.home, name='home'),
]