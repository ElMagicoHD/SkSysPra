from django.shortcuts import render



todos = [
    {   'id': 1,
        'task': 'Being a douchebag',
        'due': '15/05/2020',
        'progress': '100%'

    },
    {   'id': 2,
        'task': 'Being cool',
        'due': '16/05/2020',
        'progress': '70%'

    },
]

def overview(request):
    context = {
        'todos': todos,
        'title': 'Overview',
    }

    return render(request, 'todo/overview.html', context)

def newTodo(request):
    context = {
        'title': 'New ToDo',
    }
    return render(request, 'todo/new.html', context)

def edit(request):
    context = {
        'title': 'Edit'
    } 
    return render(request, 'todo/edit.html', context)
