from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('editlist/<str:todolist_id>', views.editTodoList, name='editlist'),
    # path('editlist/<str:todolist_id>', views.editTodoListShow, name='editlistshow'),
    path('showtodos/<str:todolist_id>', views.getOrCreateTodo, name='show'),
    path('finished/<todo_id>', views.isFinished, name='finished')
]