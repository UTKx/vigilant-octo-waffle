from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('showtodos/<str:todolist_id>', views.getOrCreateTodo, name='show')
]