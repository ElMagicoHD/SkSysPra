from django.shortcuts import render
from .models import Todo



def overview(request):
    all_todos = Todo.objects.all()

    context = {
        'todos': all_todos,
        'title': 'Overview',
    }

    return render(request, 'todo/overview.html', context)

def newTodo(request):
    context = {
        'title': 'New Todo',
    }
    return render(request, 'todo/new.html', context)

def edit(request):
    context = {
        'title': 'Edit',
    } 
    return render(request, 'todo/edit.html', context)
