from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

handler404 = 'exceptions.views.page_not_found'

handler500 = 'exceptions.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feed.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
