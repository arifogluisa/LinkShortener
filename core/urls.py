from django.urls import path
from .views import ShortenerListApiView, ShortenerCreateApiView, Redirector

urlpatterns = [
    path('',ShortenerListApiView.as_view(),name='all_links'),
    path('create/',ShortenerCreateApiView.as_view(),name='create_link'),
    path('<str:shortener_link>/',Redirector.as_view(),name='redirector')
]