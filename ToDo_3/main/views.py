from .models import Todo, TodoList
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.db.models import Prefetch
from rest_framework.response import Response
from main.serializers import TodoListSerializer, TodoRetrieveSerializer


class TodoListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TodoList.objects.all()
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['get'], url_path='completed', url_name='completed')
    def retrieve_todo_with_completed_tasks(self, request, pk=None):
        self.queryset = TodoList.objects.all().prefetch_related(
            Prefetch('todo_tasks', queryset=Todo.objects.filter(mark='D'))
        )

        instance = self.get_object()
        serializer = TodoRetrieveSerializer(instance)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TodoRetrieveSerializer
        return TodoListSerializer

