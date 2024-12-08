from django.urls import path, include
from rest_framework import routers, serializers, viewsets


urlpatterns = [
    path('api/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
