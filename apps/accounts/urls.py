from django.urls import path
from django.contrib.auth import views as auth_views
from .import views as views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='/'),name='logout'),
    path('',views.home_member,name='home-member'),
]
