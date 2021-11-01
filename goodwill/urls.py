from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('home.urls')),
    path('categories/', include('categories.urls')),
    path('product/', include('products.urls')),
    path('services/', include('services.urls')),
    path('partners/', include('partners.urls')),
    path('contact/', include('contacts.urls')),
    path('about/', include('about.urls')),
    path('site/admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
