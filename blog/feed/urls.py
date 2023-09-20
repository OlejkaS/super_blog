from django.urls import path

from . import views

handler404 = 'exceptions.views.page_not_found'

handler500 = 'exceptions.views.server_error'

urlpatterns = [
    path('', views.index, name='index')
]
