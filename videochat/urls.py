import imp
from pydoc import pathdirs
import statistics
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from base import urls # pylint: disable=unused-import
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
