from django.db import models

# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def count(self):
        return self.todos.count()

class Todo(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    is_finished = models.BooleanField(default=False)
    todolist = models.ForeignKey(TodoList, related_name='todos',on_delete=models.CASCADE)

    def __str__(self):
        return self.title