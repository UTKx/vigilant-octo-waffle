from django.shortcuts import render, redirect
from . forms import TodoListForm, TodoForm
from . models import TodoList, Todo

# Create your views here.
def list(request):
    lists = TodoList.objects.all()
    return render(request, 'main.html', {'lists':lists})

def index(request):
    form = TodoListForm()
    lists = TodoList.objects.all()
    if request.method =='POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = TodoListForm()

    context = {'form': form, 'lists': lists}
    return render(request, 'todoapp/index.html', context)

def getOrCreateTodo(request, todolist_id):
    lists = TodoList.objects.get(id=todolist_id)
    todos = Todo.objects.filter(todolist__id=todolist_id)
    form = TodoForm()
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = TodoForm()

    context = {'form': form, 'lists': lists, 'todos': todos}
    return render(request, 'todo/showtodo.html', context)