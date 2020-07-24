from django.shortcuts import render, redirect
from . forms import TodoListForm, TodoForm
from . models import TodoList, Todo

# Create your views here.

def index(request):
    listform = TodoListForm()
    todoform = TodoForm()
    lists = TodoList.objects.all()[2:]
    tasks = Todo.objects.filter(todolist__name='Task')
    if request.method =='POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('show')
    else:
        form = TodoListForm()

    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('show')
    else:
        form = TodoForm()

    context = {'listform': listform, 'todoform': todoform, 'lists': lists, 'tasks': tasks}
    return render(request, 'todoapp/index.html', context)

def getOrCreateTodo(request, todolist_id):
    lists = TodoList.objects.all()
    curlist = TodoList.objects.get(id=todolist_id)
    todos = Todo.objects.filter(todolist__id=todolist_id)
    todoform = TodoForm()
    listform = TodoListForm()
    if request.method =='POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = TodoListForm()

    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = TodoForm()

    context = {'listform': listform, 'todoform': todoform, 'lists': lists, 'curlist': curlist, 'todos': todos}
    return render(request, 'todoapp/showtodo.html', context)