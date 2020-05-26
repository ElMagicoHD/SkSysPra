from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import Todo

def overview(request):
    all_todos = Todo.objects.all()

    return render(request, 'todo/overview.html', context={'todos': all_todos,'title': 'Overview',})

# GET method
def newTodo(request):
    return render(request, 'todo/new.html', context={'title': 'New Todo'})

# POST method
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

# GET method
def edit(request, todo_id):
    tmp = Todo.objects.get(id=todo_id)
    return render(request, 'todo/edit.html', context={'todo': tmp, 'title': 'Edit'})

# POST method
def editTodo(request, todo_id):
    tmp = Todo.objects.get(id=todo_id)
    tmp.task = request.POST.get('task')
    tmp.due_date = request.POST.get('due_date')
    tmp.progress = request.POST.get('progressScrollerInput')
    tmp.save()
    return HttpResponseRedirect('/')

# POST method
def deleteTodo(request, todo_id):
    try:
        tmp = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        raise Http404("ToDo does not exist!")
    tmp.delete()
    return HttpResponseRedirect('/')

# GET method
def impressum(request):
    return render(request, 'todo/impressum.html')


