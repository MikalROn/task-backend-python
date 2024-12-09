from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, viewsets, status
from .models import Task
from .serializers import TaskSerializer
from .pagination import CustomTaskPagination



class TaskListViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = CustomTaskPagination
    
    
    @action(detail=True, methods=['get'], url_path='completar-task')
    def completar_task(self, request, pk=None):
        try:
            task = self.get_object()
            if not task.completo:
                task.completo = True
                task.save()
                serializer = TaskSerializer(task, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Task já está completa."}, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({"detail": "Task não encontrada."}, status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['get'], url_path='cancelar-conclusao-task')
    def cancelar_conclusao_task(self, request, pk=None):
        try:
            task = self.get_object()
            if task.completo:
                task.completo = False
                task.save()
                serializer = TaskSerializer(task, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Task já está incompleta."}, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({"detail": "Task não encontrada."}, status=status.HTTP_404_NOT_FOUND)

    
