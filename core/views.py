from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskListViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    