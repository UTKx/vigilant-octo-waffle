from django import forms
from django.forms import ModelForm
from . models import Todo, TodoList

class TodoListForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ['name']

class TodoForm(forms.ModelForm):
   
    class Meta:
        model = Todo
        fields = ['title']
