from django.urls import include
from django.conf.urls import handler404
from django.conf.urls.static import static

from app.views import pageNotFound
from django_hack_app_life import settings

from django.contrib import admin
from django.urls import path

from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404: handler404 = pageNotFound
