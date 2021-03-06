from django.shortcuts import render, redirect
from . forms import TodoListForm, TodoForm
from . models import TodoList, Todo

# Create your views here.


def index(request):
    listform = TodoListForm()
    todoform = TodoForm()
    lists = TodoList.objects.all()[2:]
    curlist = TodoList.objects.get(id=1)
    tasks = Todo.objects.filter(todolist__id='1')
    task_count = Todo.objects.filter(todolist__id=1).count()
    imp_count = Todo.objects.filter(todolist__id=2).count()

    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TodoListForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            instance = Todo(title=title, todolist_id='1')
            instance.save()
    else:
        form = TodoForm()

    context = {'listform': listform, 'todoform': todoform, 'lists': lists,
               'curlist': curlist, 'tasks': tasks, 'task_count': task_count, 'imp_count': imp_count}
    return render(request, 'todoapp/index.html', context)


def getOrCreateTodo(request, todolist_id):
    lists = TodoList.objects.all()[2:]
    curlist = TodoList.objects.get(id=todolist_id)
    todos = Todo.objects.filter(todolist__id=todolist_id)
    task_count = Todo.objects.filter(todolist__id=1).count()
    imp_count = Todo.objects.filter(todolist__id=2).count()
    todoform = TodoForm()
    listform = TodoListForm()

    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TodoListForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            instance = Todo(title=title, todolist_id=todolist_id)
            instance.save()
    else:
        form = TodoForm()

    context = {'listform': listform, 'todoform': todoform, 'lists': lists,
               'curlist': curlist, 'todos': todos, 'task_count': task_count, 'imp_count': imp_count}
    return render(request, 'todoapp/showtodo.html', context)


def editTodoList(request, todolist_id):
    todolist = TodoList.objects.get(id=todolist_id)
    todolist_form = TodoListForm(request.POST, instance=todolist)
    if todolist_form.is_valid():
        todolist_form.save()
        return redirect(index)
    return render(request, 'todoapp/editlist.html', {'todolist': todolist})


def deleteTodoList(request, todolist_id):
    todolist = TodoList.objects.get(id=todolist_id)
    todolist.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def editTodo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo_form = TodoForm(request.POST, instance=todo)
    if todo_form.is_valid():
        todo_form.save()
        return redirect(index)
    return render(request, 'todoapp/edittodo.html', {'todo': todo})


def deleteTodo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def isFinished(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_finished = True
    todo.save()
    return redirect(request.META.get('HTTP_REFERER'))
