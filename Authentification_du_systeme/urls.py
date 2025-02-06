from django.urls import path
from .views import *


urlpatterns = [
    path('login', login_view, name='login'),
    path('sign_up', sign_up_view, name='sign_up'),
    # path('add_products',Add_products.as_view() , name='add_products'),
    # path('update/<int:id>',update_product , name='update'),
    # path('delete/<int:id>',delete_product , name='delete'),
    # path('details/<int:id>',details_product , name='details'),
    # path('search',search_product , name='search'),
    
] 
