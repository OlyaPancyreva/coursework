from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from BestTour import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)