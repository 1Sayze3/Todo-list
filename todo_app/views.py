from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()  # Fetch all tasks from the database
    return render(request, 'todo_app/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task to the database
            return redirect('home')  # Redirect to the home page to see the updated list
    else:
        form = TaskForm()
    return render(request, 'todo_app/add_task.html', {'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)  # Get the task to delete
    task.delete()  # Delete the task from the database
    return redirect('home')  # Redirect to the home page after deletion

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Save the updated task
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_app/edit_task.html', {'form': form, 'task': task})
