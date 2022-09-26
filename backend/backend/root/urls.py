from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

from .yasg import urlpatterns as yasg_urls


urlpatterns = [     
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include('accounts.urls'))
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += yasg_urls