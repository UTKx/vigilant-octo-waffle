from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('editlist/<str:todolist_id>', views.editTodoList, name='editlist'),
    path('dellist/<str:todolist_id>', views.deleteTodoList, name='deletelist'),
    path('edittodo/<str:todo_id>', views.editTodo, name='edittodo'),
    path('deletetodo/<str:todo_id>', views.deleteTodo, name='deletetodo'),
    path('showtodos/<str:todolist_id>', views.getOrCreateTodo, name='show'),
    path('finished/<todo_id>', views.isFinished, name='finished')
]