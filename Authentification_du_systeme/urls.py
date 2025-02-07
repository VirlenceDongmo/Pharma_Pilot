from django.urls import path
from .views import *


urlpatterns = [
    path('login', login_view, name='login'),
    path('sign_up', sign_up_view, name='sign_up'),
    path('emailChecking',email_checking , name='emailChecking'),
    path('updatePassword/<str:email>',update_password , name='updatePassword'),
    path('logout',logout_view, name='logout'),
] 
