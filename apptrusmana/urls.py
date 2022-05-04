from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views as view

handler404 = 'apps.accounts.views.error_404'
handler500 = 'apps.accounts.views.error_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('',include('frontend.urls')),
    #path('home-member',include('apps.accounts.urls')),
    path('accounts/',include('apps.accounts.urls')),
    path('products/',include('apps.products.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
