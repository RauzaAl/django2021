from django.shortcuts import render
from .models import Todo, TodoList

def todo_list(request, id):

    tasks = Todo.objects.filter(list_id=id)
    list = TodoList.objects.get(id=id)

    context = {
        'tasks': tasks,
        'list': list
    }

    return render(request, 'todo_list.html', context=context)

def todo_list_completed(request, id):

    tasks = Todo.objects.filter(list_id=id, mark=True)
    list = TodoList.objects.get(id=id)

    context = {
        'tasks': tasks,
        'list': list
    }

    return render(request, 'completed_todo_list.html', context=context)