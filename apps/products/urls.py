from django.urls import path
from .import views as views

urlpatterns =[
    path('',views.list_products,name='home-member'),
    path('add_products',views.add_products,name='add-products'),
]
