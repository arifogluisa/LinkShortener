from django.shortcuts import redirect
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework import permissions

from django.views import View
from django.conf import settings

from .models import Link
from .serializers import LinkSerializer

class ShortenerListApiView(ListAPIView):
    serializer_class=LinkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Link.objects.filter(user=user)

class ShortenerCreateApiView(CreateAPIView):
    serializer_class=LinkSerializer
    permission_classes = (permissions.IsAuthenticated,)


class Redirector(View):
    def get(self,request,shortener_link,*args, **kwargs):
        shortener_link=settings.HOST_URL+'/'+self.kwargs['shortener_link']
        redirect_link=Link.objects.filter(shortened_link=shortener_link).first().original_link
        return redirect(redirect_link)