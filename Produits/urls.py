from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', welcome, name='welcome'),
    path('home', home, name='home'),
    path('add_products',Add_products.as_view() , name='add_products'),
    path('update/<int:id>',update_product , name='update'),
    path('delete/<int:id>',delete_product , name='delete'),
    path('details/<int:id>',details_product , name='details'),
    path('search',search_product , name='search'),
    path('sale/<int:id>',sale , name='sale'),
    path('billing/<int:id>',billing, name='billing'),
    path('view_bill/<int:id>',view_bill , name='view_bill'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
