from django.shortcuts import render, redirect
from .models import task
from .forms import TaskForm

# Create your views here.


def dashboard(request):
    tasks = task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo:dashboard')

    dict_obj = { 'tasks': tasks, 'form': form }
    return render(request, 'dashboard.html', dict_obj)

def edit_task(request, pk):
    task_to_edit = task.objects.get(id=pk)
    form = TaskForm(instance=task_to_edit)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task_to_edit)
        if form.is_valid():
            form.save()
        return redirect('todo:dashboard')

    dict_obj = {'form': form}
    return render(request, 'edit_task.html', dict_obj)

def delete_task(request, pk):
    task_to_delete = task.objects.get(id=pk)
    task_to_delete.delete()
    return redirect('todo:dashboard')
