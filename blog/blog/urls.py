from django.contrib import admin
from django.urls import include, path

handler404 = 'exceptions.views.page_not_found'

handler500 = 'exceptions.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feed.urls'))
]
