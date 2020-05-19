from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
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

def addTodo(request):
    #getting info from httpPost
    c = request.POST['task']
    d = request.POST['due_date']
    p = request.POST['progressScrollerInput']
    #creating Todo Object from received Inputs
    temp = Todo(task=c, due_date=d, progress = p)
    #saving item
    temp.save()
    #redirecting
    return HttpResponseRedirect('/')

def deleteTodo(request, todo_id):
    try:
        tmp = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        raise Http404("ToDo does not exist!")
    tmp.delete()
    return HttpResponseRedirect('/')




