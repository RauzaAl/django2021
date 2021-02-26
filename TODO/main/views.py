from django.shortcuts import render

def todo_list(request):

    tasks = [
        {
            'id': '1',
            'name': 'Task 1',
            'created': '10/09/2018',
            'due': '12/09/2018',
            'owner': 'admin',
            'mark': 'Done'
        },
        {
            'id': '2',
            'name': 'Task 2',
            'created': '10/09/2018',
            'due': '12/09/2018',
            'owner': 'admin',
            'mark': 'Done'
        },
        {
            'id': '3',
            'name': 'Task 3',
            'created': '10/09/2018',
            'due': '12/09/2018',
            'owner': 'admin',
            'mark': 'Done'
        },
        {
            'id': '4',
            'name': 'Task 4',
            'created': '10/09/2018',
            'due': '12/09/2018',
            'owner': 'admin',
            'mark': 'Done'
        }
    ]

    context = {
        'tasks': tasks
    }

    return render(request, 'todo_list.html', context=context)

def todo_list_complited(request):
    tasks = [
        {
            'id': '0',
            'name': 'Task 1',
            'created': '10/09/2018',
            'due': '12/09/2018',
            'owner': 'admin',
            'mark': 'Not done'
        }
    ]

    context = {
        'tasks': tasks
    }

    return render(request, 'completed_todo_list.html', context=context)