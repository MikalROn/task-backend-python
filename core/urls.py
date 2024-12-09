import core.views as views

from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'task', views.TaskListViewSet)


urlpatterns = [
    path('', include(router.urls)),
]