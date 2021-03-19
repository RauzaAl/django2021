from rest_framework import serializers
from main.models import TodoList, Todo


class TodoSerializer(serializers.ModelSerializer):
    owner_username = serializers.StringRelatedField(source='owner', read_only=True)

    class Meta:
        model = Todo
        exclude = ('owner',)


class TodoRetrieveSerializer(serializers.ModelSerializer):
    todo_tasks = TodoSerializer(many=True)

    class Meta:
        model = TodoList
        fields = ('id', 'title', 'todo_tasks')


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'
