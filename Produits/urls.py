from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('add_products',Add_products.as_view() , name='add_products'),
    path('update/<int:id>',update_product , name='update'),
    # path('add_product', views.add_product, name='add_product'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)